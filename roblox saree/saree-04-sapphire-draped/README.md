# শাড়ি ০৪ — Sapphire / Champagne, আলাদা ব্লাউজ ও খোলা কোমর

`saree-04-sapphire-draped-pants.png` হলো **585×559, 8-bit RGBA PNG**, Roblox **Classic Pants** হিসেবে ব্যবহারের জন্য। হাতের কোনো Shirt texture নেই।

ব্যবহারকারীর নতুন `saree demo 2.zip` দেখে আগের পুরো torso ঢেকে রাখা গঠন সংশোধন করা হয়েছে:

- চ্যাম্পেন রঙের cropped blouse এবং তার ওপর দিয়ে royal-blue/navy চওড়া curved pallu।
- ব্লাউজ/আঁচলের নিচে কোমর এবং শরীরের পাশে আসল alpha transparency। কোনো skin tone আঁকা হয়নি; সেখানে avatar-এর নিজস্ব skin দেখা যাবে।
- নতুন ডেমোর মতো neckline, underarm, hem ও lower-drape openings রাখা হয়েছে।
- নিচের শাড়িতে ছোট সোনালি ফুল, নরম pleats এবং cutout বরাবর সরু gold edging।

পুরোনো saree 01–03-এর full-waist mask পুনর্ব্যবহার করা হয়নি। নতুন 585×559 ডেমো `image 109.png`-এর mapped alpha থেকে বড় openings নেওয়া হয়েছে; ছোট isolated lace holes ও edge noise কিছুটা পরিষ্কার করা হয়েছে। Source RGB, source background, লেখা ও template outlines কপি করা হয়নি।

`saree-04-sapphire-draped-preview.png` সামনে ও পেছনের স্থানীয় texture-mapped preview। এটি Roblox Studio screenshot নয়।

`reference/saree-04-alpha-mask-GUIDE-ONLY.png` final alpha mask; এটি wearable file নয়। Exact panel map ও coverage note `pants-uv-layout.json`-এ আছে।

যাচাই: PNG/RGBA8, exact 585×559, final alpha ও নতুন mask-এর pixel-for-pixel মিল; neck, waist এবং side-এর probe points transparent; blouse/pallu/skirt probe points opaque। Front torso-র প্রায় 28% এবং পাশের বিভিন্ন অংশ transparent; তাই আগের মতো সম্পূর্ণ torso কাপড়ে ঢাকা নয়। Leg faces-ও এখন ইচ্ছাকৃত cutout-সহ—সব leg face opaque থাকা এখানে সঠিক শর্ত নয়।

Roblox-এ Classic Pants হিসেবে লাগান। অন্য Shirt বা upper clothing থাকলে তা কোমর/ব্লাউজ/হাতের ওপর ঢেকে দিতে পারে। Roblox Studio-তে পরীক্ষা করা হয়নি।

ভবিষ্যতের সব শাড়ির গঠনের নিয়ম [SAREE-RESEARCH.md](../SAREE-RESEARCH.md)-এ নতুন নির্দেশ অনুযায়ী হালনাগাদ করা হয়েছে।
