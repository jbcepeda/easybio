import boto3
import base64
import logging
from decouple import config

logger = logging.getLogger(__name__)

class AWSServicesConnect(object):
    def compare_faces(self, source_base64, target_base64):
        _face_matches, _matches_detail = False, None
        try:
            session = boto3.Session(
                region_name=config('AWS_REGION_NAME', cast=str),
                aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'),
                aws_session_token=config('AWS_SESSION_TOKEN')
            )
            # for p in session.available_profiles:
            #     logger.debug(session.available_profiles)
            client =session.client('rekognition')
            response=client.compare_faces(SimilarityThreshold=config('AWS_REKOGNITION_SIMILARITY_THRESHOLD', cast=int),
                                            SourceImage={'Bytes': base64.decodebytes(source_base64)},
                                            TargetImage={'Bytes': base64.decodebytes(target_base64)})
            _response = response['FaceMatches']
            _face_matches = len(_response)>0
            _matches_detail = str(_response) 
        except Exception as ex:
            logger.error(str(ex), extra={'className': self.__class__.__name__})
        return _face_matches, _matches_detail