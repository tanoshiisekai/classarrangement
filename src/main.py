from appbase import global_app
from tools.log import logger
from conf import buildhost
from conf import buildport
import dbbuilder
import apis


dbbuilder.create_db()
logger.info("app started")
global_app.run(host=buildhost, port=buildport, debug=True)
