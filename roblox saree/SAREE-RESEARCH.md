# শাড়ি: ব্যবহারকারীর স্যাম্পল বিশ্লেষণ ও ভবিষ্যতের কাজের নিয়ম

## ব্যবহারকারীর বর্তমান নির্দেশ

- এখন পাঞ্জাবি নয়, শাড়ি তৈরি হবে।
- প্রথম শাড়ি শুধু **Classic Pants**: বুক ও পা কাপড়ে ঢাকা থাকবে, দুই হাত খোলা থাকবে।
- আলাদা হাতা/বালা/হাতের নকশা কেবল পরে ব্যবহারকারী চাইলে তৈরি করতে হবে।
- ভাঁজ ও shadow যেন চোখে বেশি না লাগে; সূক্ষ্ম matte cotton texture ও নরম ভাঁজ রাখুন।
- এই চ্যাটে নতুন তৈরি wearable PNG ও preview অনুমোদিত `tohidul-gamedev/Game-projects` repository-র `main` branch-এ `roblox saree/`-এর নতুন ফোল্ডারে push করার নির্দেশ রয়েছে। বিদ্যমান কাজ বদলাবেন না।

এই নির্দেশগুলো ব্যবহারকারীর চ্যাট থেকে নেওয়া। `demoo saree.zip`-এ ছয়টি PNG রয়েছে; কোনো Markdown বা নির্দেশনামূলক document নেই।

## আপলোড করা স্যাম্পল

সব PNG **420×401 RGBA**। সেগুলোর layout সঠিক অনুপাতে থাকলেও native upload asset হিসেবে সরাসরি ধরে নেওয়া যাবে না; নতুন artwork সঠিক **585×559** canvas-এ পুনর্গঠন করতে হবে।

| ফাইল | ছবিতে দেখা গঠন | ডিজাইনের জন্য শিক্ষা |
| --- | --- | --- |
| `image 102.png` | ক্রিম-লাল শাড়ি, গোল neckline, ফুলেল cream pallu, cream skirt ও red hem | Pants-only saree silhouette এবং গোল neckline-এর মূল reference |
| `image 103.png` | mapped torso transparent; নিচের দুটি strip-এর উপরের অংশে লাল-সোনালি hand/sleeve work | আলাদা Classic Shirt-এ arm-only texture করার reference; একই layout Pants হিসেবে ব্যবহার করলে এই অংশ পায়ে পড়বে |
| `image 104.png` | লাল শাড়ি, strappy blouse, diagonal dark pallu, transparent midriff-এর কিছু অংশ | torso/leg-এ drape ধারাবাহিকতা, neckline এবং decorative bands |
| `image 105.png` | কালো শাড়ি, সাদা/রুপালি পাড়; torso ও leg-এ drape | সীমিত palette, pallu borders এবং matching lower-body fabric; এর বেশি shiny/deep folds বর্তমান পছন্দ নয় |
| `image 106.png` | 104-এর খুব কাছাকাছি red variant | 104 ও 106-এর alpha channel pixel-for-pixel একই; RGB artwork আলাদা |
| `image 107.png` | mapped torso transparent; red patterned sleeve strips | 103-এর মতো ভবিষ্যতের আলাদা Shirt sleeves-এর reference |

102/103/104/106/107-এ unused canvas pink। 105-এ অনেক unused area transparent। Pink canvas বা `Slugdolls` লেখা নতুন artwork-এ কপি করার প্রয়োজন নেই।

## Pants কেন বুক ও পা ঢাকে, হাত নয়

[Roblox-এর official Classic clothing documentation](https://create.roblox.com/docs/avatar/classic-clothing) অনুযায়ী Classic Pants torso এবং legs-এ বসে; Classic Shirt torso এবং arms-এ বসে। ছোট square T-shirt হলো front-torso graphic; সেটি wraparound sleeves বানানোর জন্য উপযুক্ত নয়।

Shirt ও Pants-এ native canvas এবং face sizes একই ধরনের হলেও **নিচের limb panels কোন অঙ্গে বসবে তা asset class নির্ধারণ করে**। Pants-এর নিচের বক্স খালি করলে হাত খোলা হবে না—পায়ের কাপড় ফাঁকা হয়ে যাবে। হাত খোলা রাখতে **Pants ব্যবহার করুন এবং কোনো sleeve Shirt যোগ করবেন না**।

## বর্তমান native UV geometry

Top-left origin; zero-based `[x,y,width,height]`। সম্পূর্ণ machine-readable map `saree-01-ivory-crimson/pants-uv-layout.json`-এ রয়েছে।

| অংশ | UP | RIGHT | FRONT | LEFT | BACK | DOWN |
| --- | --- | --- | --- | --- | --- | --- |
| Torso | 231,8,128,64 | 165,74,64,128 | 231,74,128,128 | 361,74,64,128 | 427,74,128,128 | 231,204,128,64 |
| Right leg | 217,289,64,64 | 151,355,64,128 | 217,355,64,128 | 19,355,64,128 | 85,355,64,128 | 217,485,64,64 |
| Left leg | 308,289,64,64 | 506,355,64,128 | 308,355,64,128 | 374,355,64,128 | 440,355,64,128 | 308,485,64,64 |

Left/right নাম avatar-এর শরীরের দিক, ছবির দর্শকের দিক নয়।

## প্রথম তৈরি শাড়ির alpha এবং placement

- পুরোনো **পাঞ্জাবির neck/hand mask ব্যবহার করা হয়নি**। সেই mask-এ hand cutouts আছে; Pants-এ লাগালে তা পায়ের অংশ কেটে ফেলবে।
- `image 102.png`-এর upper/front torso neckline alpha 585×559-এ resample করে নেওয়া হয়েছে; torso neckline-এ y109 পর্যন্ত প্রয়োগ করা হয়েছে।
- UP ও FRONT-এর separator y72–73-এ adjacent neck alpha চালিয়ে দেওয়া হয়েছে, যাতে opening-এর মধ্যে অস্বাভাবিক রঙের bridge না থাকে।
- দুই পায়ের সব ছয়টি face পুরো opaque। Torso neckline ছাড়া বুক, কোমর এবং পায়ের কাপড় ঢাকা।
- Final alpha সংরক্ষিত `saree-01-ivory-crimson/reference/saree-01-neck-alpha-mask-GUIDE-ONLY.png`-এ। এটি alpha channel; কাপড়ের ওপর দৃশ্যমান ছবি হিসেবে বসাবেন না।
- Native borders-এর বাইরে প্রায় 1-pixel bleed আছে; unused canvas সাদা এবং `2.94` লেখা wearable faces-এর বাইরে।
- আঁচল front থেকে shoulder UP পেরিয়ে back-এ যায়। Front leg-এর দুই half-এ shallow curved band আছে; hem height চারপাশে একই।

## পরে হাতা চাইলে

1. মূল Pants অক্ষত রাখুন।
2. নতুন **585×559 RGBA Classic Shirt** বানান।
3. Shirt-এর সব mapped torso face-এর alpha **0** রাখুন, নইলে তা Pants-এ আঁকা বুক ও আঁচল ঢেকে দিতে পারে।
4. Shirt-এর arm UP/FRONT/BACK/LEFT/RIGHT face-এ চাওয়া sleeve/bangle design বসান। Sample 103/107-এর ছোট upper-arm band না full sleeve—ব্যবহারকারীর নির্দেশ অনুযায়ী নির্বাচন করুন।
5. হাতের যে অংশ খোলা থাকবে সেখানে আসল alpha transparency দিন; skin-color বা checkerboard আঁকবেন না।
6. Pants-এর pallu/waist/leg continuity এবং Shirt-এর arm borders আলাদাভাবে পরীক্ষা করুন।
7. Preview-তে শুধু Pants এবং Pants+Shirt-সহ দৃশ্য আলাদা রাখুন, যাতে sleeve-এর প্রভাব বোঝা যায়।

## রপ্তানি ও যাচাই

একটি folds-সহ version, PNG/RGBA8, exact 585×559। Source sample branding, UV outline, visible masks, guide text, mannequin অথবা background wearable faces-এ নয়। Check neckline transparency, বুকের কাভারেজ, সব leg faces, leg center join, pallu seam ও hem। Roblox Studio-তে পরীক্ষা না করলে সেভাবে পরীক্ষা হয়েছে বলে দাবি করবেন না।
