import os

TEMP_TAR_GZ_FILENAME = '/tmp/fairing.layer.tar.gz'
DEFAULT_IMAGE_NAME = 'fairing-job'
DEFAULT_BASE_IMAGE = 'gcr.io/kubeflow-images-public/fairing:dev'
DEFAULT_REGISTRY = 'index.docker.io'
# DEFAULT_DEST_PREFIX = '/app/'
DEFAULT_DEST_PREFIX = os.path.expanduser('~')

DEFAULT_CONTEXT_FILENAME = '/tmp/fairing.context.tar.gz'
DEFAULT_GENERATED_DOCKERFILE_FILENAME = '/tmp/Dockerfile'

GOOGLE_CREDS_ENV = 'GOOGLE_APPLICATION_CREDENTIALS'
