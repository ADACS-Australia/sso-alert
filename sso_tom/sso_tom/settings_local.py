from decouple import config as dotenv


# To add a new topic - add one here.
TOPICS = [
    'fink_early_sn_candidates_ztf',
    'fink_sn_candidates_ztf',
    'fink_sso_ztf_candidates_ztf',
    'fink_sso_fink_candidates_ztf',
    'fink_kn_candidates_ztf',
    'fink_early_kn_candidates_ztf',
    'fink_rate_based_kn_candidates_ztf',
    'fink_microlensing_candidates_ztf',
    'fink_blazar_ztf',
]


# Function to generate ALERT_STREAMS dynamically
def generate_alert_streams():
    return [
        {
            'ACTIVE': True,
            'NAME': 'tom_fink.alertstream.FinkAlertStream',
            'OPTIONS': {
                'URL': dotenv('FINK_CREDENTIAL_URL', default='set FINK_CREDENTIAL_URL value in environment'),
                'USERNAME': dotenv('FINK_CREDENTIAL_USERNAME', default='set FINK_CREDENTIAL_USERNAME value in environment'),
                'GROUP_ID': dotenv('FINK_CREDENTIAL_GROUP_ID', default='set FINK_CREDENTIAL_GROUP_ID value in environment'),
                'TOPIC': topic,
                'MAX_POLL_NUMBER': dotenv("FINK_MAX_POLL_NUMBER", default=1e10),
                'TIMEOUT': dotenv('FINK_TIMEOUT', default=10, cast=int),
                'TOPIC_HANDLERS': {
                    'fink.stream': 'sso_alerts.alert_handler.alert_logger',
                },
            },
        } for topic in TOPICS
    ]


# Generate ALERT_STREAMS dynamically
ALERT_STREAMS = generate_alert_streams()

SITE_URL = ''


SERVER_EMAIL = 'noreply@supercomputing.swin.edu.au'
EMAIL_HOST = 'mail.swin.edu.au'
EMAIL_FROM = 'hpc-support@swin.edu.au'
