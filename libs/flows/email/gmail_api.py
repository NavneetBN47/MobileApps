from SAF.email.imap_client import IMAPClient
from SAF.email.gmail_client import GmailClient

from selenium.common.exceptions import *
import logging
import time
import re


class NoEmailException(Exception):
    pass

class CONST():
    GMAIL_IMAP = "imap.gmail.com"
    SENDER_EMAIL = "donotreply@hpeprint.com"
    GMAIL_SUBJECT = "ePrint mobile registration"
    HPID_VERIFICATION_EMAIL = ">[A-Z0-9]{6}<"
    INVITATION_EMAIL = r"https://click\.email\.hpsmart\.com/u/\?qs=[a-f0-9]+"

class GmailImap(object):
    def __init__(self, username, pwd):
        """
        :type cfg: MobiConfig
        :param cfg:
        """
        self.gmail = IMAPClient(CONST.GMAIL_IMAP,username, pwd)


    def delete_messages_pin_code(self):
        """
        Delete all messages about pin code
        """
        self.gmail.delete_emails_by_sender_email(CONST.SENDER_EMAIL)


    def get_subject_with_sender_email(self, sender_email):
        """
        Get Subject content from an email with its sender_email

        :param sender_email: sender's email
        :return: Subject content
        """
        subject_content = self.gmail.get_newest_unread_message_with_sender_email(sender_email=sender_email)[0]
        return subject_content


    def delete_messages_with_sender_email(self, sender_email):
        """
        Delete all massages corresponding to sender
        """
        self.gmail.delete_emails_by_sender_email(sender_email=sender_email)


class GmailAPI(object):
    def __init__(self, credential_path):
        """
        Due to security reasons we do not cache any Google API tokens in the test repository.
        If you want a copy of the API token for the qamobiauto@gmail.com account 
        Please contact Hai Tran
        """
        self.gmail = GmailClient(credential_path =credential_path)


    def send_email(self, to='', subject='', content='', file_paths=[]):
        """
        Send an email

        :param to: recipient
        :type to: str
        :param subject: subject of the email
        :type subject: str
        :param content: content of the email
        :type content: str
        :param file_paths: file path of the attachment
        :type file_paths: list
        :return: message: a message resource
        """
        if file_paths:  # has attachment
            message = self.gmail.create_message_with_attachment(
                to=to, subject=subject, message_text=content, file_paths=file_paths)
        else:  # empty = no attachment
            message = self.gmail.create_message(to=to, subject=subject, message_text=content)
        draft = self.gmail.create_draft(message)
        self.gmail.send_draft(draft)
        return True


    def mark_email_as_read(self, msg_id):
        """
        Mark the message as read.

        :param msg_id: message id
        :type msg_id: str
        """
        self.gmail.modify_message_label(msg_id=msg_id, remove_label=['UNREAD'])


    def mark_email_as_unread(self, msg_id):
        """
        Mark the message as unread.

        :param msg_id: message id
        :type msg_id: str
        """
        self.gmail.modify_message_label(msg_id=msg_id, add_label=['UNREAD'])


    def delete_email(self, msg_id):
        """
        Move the message into Trash.

        :param msg_id: message id : [{'id': "","threadid": ""},{'id': "","threadid": ""},...]
        :type msg_id: str
        """
        if type(msg_id) is not list:
            msg_id = [msg_id]
        for _id in msg_id:
            self.gmail.trash_message(msg_id=_id['id'])


    def get_attachments(self, msg_id, store_dir=''):
        """
        Retrieve the attachments of a message; if store_dir is not specified, just return the names.

        :param msg_id: The ID of the Message containing attachments.
        :type msg_id: str
        :param store_dir: The directory used to store attachments.
        :type store_dir: str
        :return files: a list of file names for the attachments
        """
        return self.gmail.get_attachment(msg_id, store_dir)

    def delete_hpid_verification_code_email(self, to, timeout=60, raise_e=False):
        """
        Delete Email for HPID verification code
        :param to: 'to' email
        """
        msgs = self.search_for_messages(q_to=to, q_from="no-reply@stg.cd.id.hpcwp.com", q_unread=True, timeout=timeout, raise_e=raise_e)
        if msgs:
            self.delete_email(msgs)
            return True
        return False


    def delete_all_messages_from_inbox(self):
        """
        Remove all messages in Inbox.
        """
        msgs = self.search_for_messages(custom_query='in:inbox')
        logging.info('Removing {} messages...'.format(len(msgs)))
        self.delete_email(msgs)

    def batch_delete_from_sender(self, sender_email):
        """
        Batch delete all emails from the specified sender.
        :param sender_email: The sender's email address.
        :type sender_email: str
        :return: Number of deleted messages.
        """
        try:
            messages = self.search_for_messages(q_from=sender_email)
            if not isinstance(messages, list) or len(messages) == 0:
                logging.info(f"No messages found from {sender_email}")
                return 0
            logging.info(f"Found {len(messages)} messages from {sender_email}")
            msg_ids = [msg['id'] for msg in messages if 'id' in msg]
            count = 0
            # Gmail API allows up to 1000 IDs per batchDelete
            for i in range(0, len(msg_ids), 999):
                batch = msg_ids[i:i+999]
                self.gmail.service.users().messages().batchDelete(userId='me', body={'ids': batch}).execute()
                count += len(batch)
            logging.info(f"Batch deleted {count} messages from {sender_email}")
            return count
        except Exception as error:
            logging.error(f"An error occurred: {error}")
            return False
    
    def get_content_from_email(self, query, to, since, q_from='', clear_msg=True, timeout=60, raise_e=True):
        """
        Always gets the latest unread email
        :param query: specific search in email e.g. HPID verification code, invitation url
        :param to: Email it was targeted
        :param since: Get the latest email since (ctime)
        :param clear_msg: delete the email after getting code
        :return: desired content grabbed using regular expression
        """
        msgs = self.search_for_messages(q_to=to, q_from=q_from, q_unread=True, custom_query="after:" + str(since), timeout=timeout, raise_e=raise_e)
        if msgs:
            msg = self.gmail.get_message(msgs[0]['id'], 'raw')
            content = self.gmail.decode_raw_message(msg)
            self.mark_email_as_read(msgs[0]['id'])
            if clear_msg:
                self.delete_email(msgs)
            data = re.search(query, content).group()
            if query == CONST.HPID_VERIFICATION_EMAIL:
                return data[1:-1]
            else:
                return data
        return False
    
    
    def search_for_messages(self, q_to='', q_from='', q_subject='', q_label='', q_unread=False, q_content='', custom_query='', timeout=3, raise_e=False):
        """
        Search for all Messages matching the criteria.

        :param q_to: recipient's email address
        :type q_to: str
        :param q_from: sender's email address
        :type q_from: str
        :param q_subject: subject of email
        :type q_subject: str
        :param q_label: tags/labels of the email
        :type q_label: str
        :param q_unread: whether the email is unread or not
        :type q_unread: bool
        :param q_content: any words from within the email
        :type q_content: str

        :return messages: List of Messages IDs that match the criteria of the query. Note that the
                          returned list contains Message IDs, you must use get with the
                          appropriate ID to get the details of a Message; or [].
        """
        start_time = time.time()
        while time.time() < start_time + timeout:
            message_id = self.gmail.list_messages_matching_query(self.gmail.query_builder(
            q_to=q_to, q_from=q_from, q_subject=q_subject, q_label=q_label, q_unread=q_unread, q_content=q_content) + custom_query)

            if message_id:
                logging.info("{}:[Message Found! ID: {}]".format(self.search_for_messages.__name__,message_id ))
                return message_id

        if raise_e:
            raise TimeoutException("Took longer than {} seconds to retrieve email from Gmail".format(timeout))
        else:
            return False

    #******************************************************************************************************************
    #                                   Send your own email and delete what you sent                                  *
    #******************************************************************************************************************
    def send_email_with_keyword(self, to='', subject='', content='', keyword = ''):
        """
        Send an email

        :param to: recipient
        :type to: str
        :param subject: subject of the email
        :type subject: str
        :param content: content of the email
        :type content: str
        :return: message: a message resource
        """
        keyword = self.cfg.get("DEVICE", "udid")
        message = self.gmail.create_message(to=to, subject=subject, message_text="{}_{}".format(content, keyword))
        draft = self.gmail.create_draft(message)
        self.gmail.send_draft(draft)
        return True