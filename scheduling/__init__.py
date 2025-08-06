from zoneinfo import ZoneInfo

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from configuration import environment_configuration_bean
from configuration.logging_configuration import logger as log
from scheduling.upload_to_drive_scheduler import schedule

scheduler = BackgroundScheduler(timezone=ZoneInfo("UTC"))
cron_expr_every_five_minutes = CronTrigger.from_crontab("*/5 * * * *")
scheduler.add_job(schedule, cron_expr_every_five_minutes)
if environment_configuration_bean.get("ACTIVE_PROFILE") == "docker":
    log.info("Starting scheduler in Docker environment")
    scheduler.start()
