import paho.mqtt.client as mqtt  
import time  
import json

# تنظیمات سرور EMQX  
broker = "0.0.0.0"  # آدرس سرور EMQX  
port = 1883  # پورت پیش‌فرض برای MQTT  
topic = "your/topic"  # موضوع (topic) که می‌خواهید پیام‌ها را در آن منتشر کنید  

def publish(client):  
    msg_count = 1  
    while True:  
        time.sleep(1)  
        msg = f"messages: {msg_count}"  
        result = client.publish(topic, msg)  
        # result: [0, 1]  
        status = result[0]  
        if status == 0:  
            print(f"Send `{msg}` to topic `{topic}`")  
        else:  
            print(f"Failed to send message to topic {topic}")  
        msg_count += 1  
        if msg_count > 5:  
            break  

def main():  
    client = mqtt.Client()  

    # در صورت نیاز به اعتبارسنجی (مثلاً اگر EMQX نیاز به نام کاربری و کلمه عبور داشته باشد):  
    # client.username_pw_set("your_username", "your_password")  

    client.connect(broker, port)  

    # شروع به انتشار پیام‌ها  
    publish(client)  

    client.loop_start()  # شروع به پردازش پیام‌ها در پس‌زمینه  
    client.loop_stop()  # متوقف کردن پردازش پس‌زمینه بعد از اتمام انتشار  

if __name__ == "__main__":  
    main()