# অন্য AI-কে দিয়ে একই নিয়মে পাঞ্জাবি বানানোর প্যাক

এটি **Roblox Classic Shirt পাঞ্জাবি** তৈরির reference pack। অনুমোদিত PNG, exact alpha mask, panel coordinates ও কপি করে দেওয়ার prompt একসঙ্গে আছে।

## যেভাবে ব্যবহার করবে

1. ZIP extract করো।
2. অন্য AI-কে প্রথমে `01-approved-layout.png`, `02-uv-overlay-GUIDE-ONLY.png` এবং `03-shirt-alpha-mask.png` দাও। File upload থাকলে পুরো ZIP-ই দিতে পারো।
3. পছন্দের ধরন বোঝাতে `04`, `05` বা `06` থেকে একটি example দাও। বাস্তব পাঞ্জাবির reference photo থাকলে সেটিও দাও।
4. `AI-PROMPT.md`-এর পুরো লেখা কপি করে পাঠাও। শেষের চারটি ঘরে কয়টি ডিজাইন, রং/স্টাইল ও reference-এর তথ্য লিখো।
5. Final result হিসেবে 585×559 RGBA PNG চাও। শুধু preview পেলে wearable PNG-টিও নিতে হবে।

একবারে কম attachment দেওয়া গেলে প্রথম তিনটি ফাইল সবচেয়ে প্রয়োজনীয়। Plain style বোঝাতে `06`, gamcha style-এর জন্য `04`, wrap coat-এর জন্য `05` বেছে নাও।

## কোন ছবির কাজ কী

| ফাইল | ব্যবহার |
| --- | --- |
| 01-approved-layout.png | গলা, হাত, artwork scale, সাদা canvas ও2.94-এর অনুমোদিত layout |
| 02-uv-overlay-GUIDE-ONLY.png | বক্সের অবস্থান বুঝবে; এর outline final PNG-তে যাবে না |
| 03-shirt-alpha-mask.png | Software-এ final alpha হিসেবে বসাবে; এটি gray/black/white mask, পোশাকের texture নয় |
| 04-style-gamcha.png | পাঞ্জাবির ওপর gamcha/uttoriyo layering-এর উদাহরণ |
| 05-style-wrap-coat.png | বড় decorative wrap layer ও coordinated sleeves/back-এর উদাহরণ |
| 06-style-charcoal.png | কালো কাপড়েও বুনন, সেলাই ও নরম ভাঁজ রাখার উদাহরণ |
| uv-layout.json | Zero-based `[x,y,width,height]`-এ exact panel মাপ |
| tools/finalize-shirt.sh | আগে তৈরি করা native composition-এ approved alpha ও2.94 বসায় |
| tools/validate_png.py | Final PNG-এর মাপ, channel, mask ও basic canvas checks করে |

ভালো ফলের জন্য অন্য AI-এর ছবি তৈরি করার পাশাপাশি নির্দিষ্ট pixel মাপে PNG edit এবং alpha channel নিয়ন্ত্রণের সুবিধা থাকা দরকার। শুধু প্রম্পট একা সব AI-তে একই মান বা pixel-accurate output নিশ্চিত করে না; দেওয়া মাস্ক ও যাচাইয়ের নিয়ম এ জন্যই রাখা হয়েছে।

এখানে নতুন পোশাক তৈরি করা হয়নি; আগের অনুমোদিত উদাহরণগুলো training/reference হিসেবে একত্র করা হয়েছে। Guide overlay এবং mask reference; সেগুলো Roblox-এ upload করার জন্য নয়।
