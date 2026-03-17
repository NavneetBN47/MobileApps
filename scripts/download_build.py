#!/usr/bin/env python3
"""
Windows build download script.
Usage examples:
    # Download Windows HPX rebrand_pie build (default)
    python download_build.py --project HPX
    
    # Download Windows HPX rebrand_stage build
    python download_build.py --project HPX --stack rebrand_stage
    
    # Download Windows HPX pie build (non-rebrand)
    python download_build.py --project HPX --stack pie
    
    # Download Windows HPAI debug build
    python download_build.py --project HPAI --build_type debug
"""

import sys
import os

# Add MobileApps parent directory to sys.path temporarily for imports
_script_dir = os.path.dirname(os.path.abspath(__file__))
_mobile_apps_dir = os.path.dirname(_script_dir)
_parent_dir = os.path.dirname(_mobile_apps_dir)
sys.path.insert(0, _parent_dir)

import argparse
import logging
from pathlib import Path

from MobileApps.libs.app_package.github_api import github_api_factory
from MobileApps.libs.ma_misc import ma_misc

# Remove from sys.path after imports are done
sys.path.remove(_parent_dir)

def download_build(project_name=None, build_type=None, stack=None, build_version=None, 
                   build_number=None, release_type=None, save_location="./", unzip=False):
    """
    Windows build download function.
    
    Args:
        project_name: Project name (HPX or HPAI)
        build_type: Type of build
        stack: Stack/variant for Windows (e.g., "rebrand", "regular")
        build_version: Major version (e.g., "8.6.1")
        build_number: Build number (e.g., "25")
        release_type: "daily" or "stable"
        save_location: Path to save the build
        unzip: Whether to unzip the downloaded file
    """
    try:
        # Set defaults for Windows
        if project_name is None:
            project_name = "HPX"
        
        # For Windows, use stack as the actual build_type
        if stack is None:
            stack = "rebrand_pie"  # Default stack for Windows
        
        # Stack becomes the build_type for Windows
        build_type = stack
        
        if release_type is None:
            release_type = "daily"
        
        # Windows builds are too large for database (1GB+), skip DB
        logging.info("Database skipped for Windows (files too large)")
        
        # Create GitHub API instance
        logging.info(f"Initializing GitHub API for Windows {project_name}...")
        github_api = github_api_factory(
            platform="WINDOWS",
            project_name=project_name,
            db_utils=None
        )
        
        # Build info message
        version_info = ""
        if build_version and build_number:
            version_info = f" version {build_version}.{build_number}"
        elif build_version:
            version_info = f" version {build_version}.x (latest)"
        else:
            version_info = " (latest)"
        
        release_info = f" from {release_type} releases"
        logging.info(f"=== Downloading Windows {project_name} {build_type} build{version_info}{release_info} ===")
        
        # Get build information from GitHub API
        url, actual_build_version, actual_daily_version, app_info = github_api.find_build(
            build_type=build_type,
            build_version=build_version,
            build_number=build_number,
            release_type=release_type
        )
        
        # Log build details
        logging.info(f"✓ Found build:")
        logging.info(f"  - Build Version: {actual_build_version}")
        logging.info(f"  - Build Number: {actual_daily_version}")
        logging.info(f"  - File Name: {app_info}")
        
        # Check if build already exists (zip file)
        build_exists = False
        existing_build_path = None
        
        save_path_obj = Path(save_location)
        if save_path_obj.exists():
            # Check for existing zip file with the version number
            for item in save_path_obj.iterdir():
                if item.is_file() and item.suffix == '.zip':
                    # Check if the version number is in the zip file name
                    if actual_build_version in item.name:
                        build_exists = True
                        existing_build_path = item
                        logging.info(f"✓ Build already exists: {item.name}")
                        logging.info(f"  Location: {item}")
                        logging.info(f"  Skipping download...")
                        break
        
        # Download only if build doesn't exist
        if not build_exists:
            logging.info(f"  Build not found in {save_location}")
            logging.info(f"  Downloading build...")
            ma_misc.download_build_to_local(url, save_path=save_location, auth_header=github_api.auth_header, unzip=unzip)
            logging.info(f"✓ Build downloaded successfully to: {save_location}")
            
            # Find the downloaded zip file
            for item in save_path_obj.iterdir():
                if item.is_file() and item.suffix == '.zip' and actual_build_version in item.name:
                    existing_build_path = item
                    break
        
        # Always return just the directory path
        final_location = save_location
        
        # Return build info for display
        return {
            'version': actual_build_version,
            'build_number': actual_daily_version,
            'filename': app_info,
            'location': final_location
        }
        
    except Exception as e:
        logging.error(f"✗ Failed to download build: {str(e)}")
        import traceback
        logging.debug(traceback.format_exc())
        return False


def main():
    # Configure logging to stdout for pipeline visibility
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    parser = argparse.ArgumentParser(
        description="Windows build download script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Windows stacks (use --stack parameter):
  - rebrand_pie (default - rebrand integration)
  - rebrand_stage (rebrand stage)
  - rebrand_production (rebrand production)
  - rebrand_development (rebrand development)
  - pie (integration)
  - stage
  - production
  - development

Examples:
  # Download Windows HPX rebrand_pie build (default)
  python download_build.py --project HPX
  
  # Download Windows HPX rebrand_stage build
  python download_build.py --project HPX --stack rebrand_stage
  
  # Download Windows HPX pie build (non-rebrand)
  python download_build.py --project HPX --stack pie
  
  # Download Windows HPX production build
  python download_build.py --project HPX --stack production
  
  # Download Windows HPAI debug build
  python download_build.py --project HPAI --build_type debug
  
  # Download to specific location
  python download_build.py --project HPX --save_location ./builds
  
  # Download stable release
  python download_build.py --project HPX --release_type stable
        """
    )
    
    parser.add_argument(
        '--project',
        type=str,
        default="HPX",
        help='Project name: HPX or HPAI (default: HPX)'
    )
    
    parser.add_argument(
        '--build_type',
        type=str,
        default=None,
        help='Type of build (generally not used for Windows, use --stack instead)'
    )
    
    parser.add_argument(
        '--stack',
        type=str,
        default=None,
        choices=['rebrand_pie', 'rebrand_stage', 'rebrand_production', 'rebrand_development', 
                 'pie', 'stage', 'production', 'development'],
        help='Stack for Windows builds (default: rebrand_pie)'
    )
    
    parser.add_argument(
        '--build_version',
        '--version',
        type=str,
        default=None,
        dest='build_version',
        help='Major version of the build (e.g., "8.6.1"). Alias: --version'
    )
    
    parser.add_argument(
        '--build_number',
        type=str,
        default=None,
        help='Build number (e.g., "25"). Requires --build_version'
    )
    
    parser.add_argument(
        '--release_type',
        type=str,
        default=None,
        choices=['daily', 'stable'],
        help='Release type: daily or stable (default: daily)'
    )
    
    parser.add_argument(
        '--save_location',
        type=str,
        default='/tmp/builds',
        help='Directory to save the build (default: /tmp/builds)'
    )
    
    parser.add_argument(
        '--unzip',
        action='store_true',
        help='Unzip the downloaded file locally (default: False, keeps as zip)'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.build_number and not args.build_version:
        parser.error("--build_number requires --build_version")
    
    # Validate project name for Windows
    if args.project and args.project.upper() not in ["HPX", "HPAI"]:
        parser.error("Windows project must be HPX or HPAI")
    
    # Create save location if it doesn't exist
    Path(args.save_location).mkdir(parents=True, exist_ok=True)
    
    # Download the build
    result = download_build(
        project_name=args.project,
        build_type=args.build_type,
        stack=args.stack,
        build_version=args.build_version,
        build_number=args.build_number,
        release_type=args.release_type,
        save_location=args.save_location,
        unzip=args.unzip
    )
    
    if result and isinstance(result, dict):
        print(f"\n{'='*70}")
        print(f"BUILD INFORMATION:")
        print(f"  Version:      {result['version']}")
        print(f"  Build Number: {result['build_number']}")
        print(f"  File Name:    {result['filename']}")
        print(f"  Location:     {result['location']}")
        print(f"{'='*70}")
        print(f"\nBUILD_FILENAME={result['filename']}")
        
        # Set Azure DevOps pipeline variables for consumption in next stages
        print(f"##vso[task.setvariable variable=BUILD_VERSION;isOutput=true]{result['version']}")
        print(f"##vso[task.setvariable variable=BUILD_NUMBER;isOutput=true]{result['build_number']}")
        print(f"##vso[task.setvariable variable=BUILD_FILENAME;isOutput=true]{result['filename']}")
        print(f"##vso[task.setvariable variable=BUILD_LOCATION;isOutput=true]{result['location']}")
    
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
