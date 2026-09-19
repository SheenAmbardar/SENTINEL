import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD"
    )
    return connection


if __name__ == "__main__":
    try:
        conn = get_connection()

        if conn.is_connected():
            print("✅ Successfully connected to MySQL!")

        conn.close()

    except Exception as e:
        print("Connection Error:", e)