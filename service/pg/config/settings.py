from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

REPO_DIR = BASE_DIR.parent.parent

sys.path.append(str(REPO_DIR))

from common.config.settings import *

INSTALLED_APPS += [
    # * Apps
    'apps.pg.apps.PGConfig',

    # * Packages
    'django_grpc',
]

# * ------------------------------- gRPC -------------------------------
GRPCSERVER = {
    'servicers': [
        'apps.pg.grpc.register',
    ],
    'maximum_concurrent_rpcs': None,
    'options': [
        (
            'grpc.max_receive_message_length',
            1024 * 1024 * 100,
        ),
    ],
}
# * --------------------------------------------------------------------
