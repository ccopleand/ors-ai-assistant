import time
from scheduler import TaskScheduler
from tasks.email_monitoring import check_and_log_cra_emails
from tasks.sharepoint_checker import check_outstanding_items
from tasks.protocol_trigger import run_protocol_toolkit_if_updated
from tasks.auto_response import send_urgent_reply_if_needed
from config import CHECK_INTERVAL_MINUTES

def main():
    print("=== ORS AI Assistant: Full-Scope Automation Engine ===")

    # Task registry: plug-and-play modular jobs
    scheduler = TaskScheduler()
    scheduler.add_task("CRA Inbox Monitor", check_and_log_cra_emails)
    scheduler.add_task("SharePoint Outstanding Review", check_outstanding_items)
    scheduler.add_task("Protocol Trigger Toolkit", run_protocol_toolkit_if_updated)
    scheduler.add_task("CRA Urgent Auto-Responder", send_urgent_reply_if_needed)

    # Infinite background loop (can be adapted for APScheduler or Celery later)
    while True:
        print("\n[Cycle Start] Running all registered automation tasks...\n")
        scheduler.run_all()
        print(f"\n[Cycle Complete] Sleeping for {CHECK_INTERVAL_MINUTES} minutes...\n")
        time.sleep(CHECK_INTERVAL_MINUTES * 60)

if __name__ == "__main__":
    main()