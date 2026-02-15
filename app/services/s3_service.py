import boto3
from uuid import uuid4
from app.core.config import settings


s3_client = boto3.client(
    "s3",
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
)


def upload_file_to_s3(file):
    file_extension = file.filename.split(".")[-1]
    unique_filename = f"{uuid4()}.{file_extension}"

    s3_client.upload_fileobj(
        file.file,
        settings.S3_BUCKET_NAME,
        unique_filename,
        ExtraArgs={"ContentType": file.content_type},
    )

    file_url = (
        f"https://{settings.S3_BUCKET_NAME}.s3."
        f"{settings.AWS_REGION}.amazonaws.com/{unique_filename}"
    )

    return file_url
