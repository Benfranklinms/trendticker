from config.db import get_db_connection
from datetime import datetime

def save_or_update_product(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, price, notified FROM trackers WHERE url = %s AND email = %s",
        (data["url"], data["email"])
    )
    existing = cursor.fetchone()

    if existing:
        tracker_id, old_price, already_notified = existing

        cursor.execute("""
            UPDATE trackers
            SET title = %s,
                price = %s,
                image = %s,
                notified = %s,
                last_checked = %s
            WHERE id = %s
        """, (
            data["title"],
            data["price"],
            data["image"],
            data["notified"],
            datetime.now(),
            tracker_id
        ))

    else:
        cursor.execute("""
            INSERT INTO trackers (url, title, price, target_price, email, image, notified, last_checked)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            data["url"],
            data["title"],
            data["price"],
            data["target_price"],
            data["email"],
            data["image"],
            data["notified"],
            datetime.now()
        ))

    conn.commit()
    cursor.close()
    conn.close()