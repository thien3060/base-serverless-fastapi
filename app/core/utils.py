from app.core.config import settings


def create_public_s3_url(
    key, bucket=settings.NEXTFLOW_S3_BUCKET, region=settings.AWS_DEFAULT_REGION
):
    url = f"https://{bucket}.s3.{region}.amazonaws.com/{key}"
    return url
