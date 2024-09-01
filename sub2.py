import paho.mqtt.client as mqtt  

# تنظیمات سرور EMQX  
broker = "0.0.0.0"  # آدرس سرور EMQX  
port = 1883 # پورت پیش‌فرض برای MQTT  
topic = "your/topic"  # موضوع (topic) که می‌خواهید در آن مشترک شوید  

def subscribe(client: mqtt.Client):  
    def on_message(client, userdata, msg):  
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")  

    # ثبت Callback برای دریافت پیام  
    client.on_message = on_message  
    client.subscribe(topic)  

def main():  
    client = mqtt.Client()  

    # در صورت نیاز به اعتبارسنجی (مثلاً اگر EMQX نیاز به نام کاربری و کلمه عبور داشته باشد):  
    # client.username_pw_set("your_username", "your_password")  

    client.connect(broker, port)  

    subscribe(client)  

    client.loop_forever()  # شروع به گوش دادن برای پیام‌ها  

if __name__ == "__main__":  
    main()