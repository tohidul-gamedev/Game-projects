# শাড়ি: ব্যবহারকারীর স্যাম্পল বিশ্লেষণ ও ভবিষ্যতের কাজের নিয়ম



## সর্বশেষ ডিফল্ট — প্রতিটি শাড়ির সঙ্গে matching হাতা, কোনো প্রিভিউ নয়

ব্যবহারকারীর সর্বশেষ নির্দেশ: প্রতিবার শাড়ি বানাতে বললেই প্রতিটি ডিজাইনের জন্য **দুটি আলাদা 585×559 RGBA8 wearable PNG** দিতে হবে—(১) Classic Pants শাড়ি, (২) matching short-sleeve Classic Shirt। হাতা আলাদাভাবে চাইতে হবে না। Shirt-এর সব mapped torso face alpha 0 থাকবে, যাতে Pants-এর blouse/pallu এবং অনুমোদিত open waist/side cutouts বদলে না যায়। Forearm ও hands খোলা থাকবে, যদি ভিন্ন নির্দেশ না থাকে।

**প্রিভিউ, 3D mockup, thumbnail, comparison board বা preview file তৈরি/প্রকাশ করবেন না**, ব্যবহারকারী পরে আলাদা করে না চাইলে। শুধু final wearable PNG এবং একাধিক হলে ZIP দিন। চূড়ান্ত native PNG সরাসরি দেখে ও dimensions/mode/alpha/layering checks দিয়ে যাচাই করুন। সব final PNG/ZIP অনুমোদিত GitHub repository-তে push করুন। এই নির্দেশ আগের optional-sleeve এবং preview workflow-কে প্রতিস্থাপন করেছে।

নতুন উদাহরণ: `sets-08-09/`—ivory/terracotta botanical এবং peacock-blue/violet ikat, প্রতিটির matching sleeve Shirt-সহ। এই collection-এ চারটি PNG এবং একটি ZIP আছে; কোনো preview file নেই।

## ব্যবহারকারীর নিশ্চিত করা শাড়ি ও আলাদা হাতার নিয়ম

ব্যবহারকারী শাড়ি ০৪–০৬-এর আলাদা blouse, broad pallu, true open waist/side cutouts এবং unique motif-based styles পছন্দ করেছেন। ভবিষ্যতে শাড়ি চাইলে এই গঠন ধরে নতুন unique design দিন; আগের full-torso কাপড়ে ঢাকা গঠন ফিরিয়ে আনবেন না। হাতে কাজ চাইলে শাড়ির Pants এবং sleeves-এর Shirt **দুটি আলাদা wearable PNG** দিতে হবে। সর্বশেষ নির্দেশ অনুযায়ী শুধু শাড়ি বললেও আলাদা matching হাতার Shirt দিতে হবে।

হাতা-সহ সম্পূর্ণ উদাহরণ: `saree-07-emerald-rose-set/`। Pants-এ শাড়ি ও blouse আছে; Shirt-এ শুধু arms। Shirt-এর mapped torso UP/FRONT/BACK/LEFT/RIGHT/DOWN-এ **প্রতিটি pixel alpha 0**—তাতে Pants-এর blouse/pallu/midriff ঢেকে যায় না। Arm top cap opaque; vertical arm face-এর প্রথম প্রায় 56 pixels-এ short sleeve, নিচের forearm ও hand/DOWN transparent।

নতুন `saree hand.zip`-এর 103/107 source **586×559 RGBA**, native 585×559 নয়। Artwork native coordinates-এ পুনর্গঠন করতে হবে। 103-এ কেন্দ্রীয় arm columns y355–403 পর্যন্ত opaque, 107-এ y355–410। Source-এর mapped torso মূলত transparent; DOWN torso-র মধ্যে source lettering আছে, যা নতুন Shirt-এ কপি করলে শাড়ির ওপর অপ্রয়োজনীয় লেখা/কাপড় বসতে পারে। তাই সব mapped torso faces পরীক্ষা করে সম্পূর্ণ clear রাখতে হবে। Source background, template outline এবং branding কপি নয়।

সর্বশেষ নির্দেশ অনুযায়ী preview file তৈরি করবেন না; native PNG এবং Shirt/Pants layering alpha পরীক্ষা করুন। PNG file role স্পষ্ট করুন: **Classic Pants** বনাম **Classic Shirt**, square T-shirt graphic নয়। Native RGBA8 এবং per-face alpha যাচাই করুন; layering-এ Pants torso অপরিবর্তিত থাকে কি না pixel comparison করুন। উদাহরণগুলোর style preference ও এই নিয়ম repository notes-এ রাখা হলো, যাতে ভবিষ্যতের কাজেও পুনরায় ব্যবহার করা যায়।

## সর্বশেষ সংশোধন — কোমর ও পাশের আসল transparency বাধ্যতামূলক

ব্যবহারকারী আগের saree 01–03-এর পুরো কোমর ঢাকা গঠন সংশোধন করতে বলেছেন। নতুন `saree demo 2.zip`-এ native 585×559 RGBA `image 108.png`, `109.png`, `110.png` দিয়েছেন। ব্লাউজ, তার ওপর বাঁক নেওয়া চওড়া আঁচল এবং নিচের শাড়ি আলাদা বোঝাতে কোমর/মিডরিফ, underarm ও উপযুক্ত পাশে আসল alpha cutout রাখুন। শুধু Pants ব্যবহার করার অর্থ সব torso pixel opaque রাখা নয়। Skin colour বা সাদা/কালো রং এঁকে ফাঁকা বোঝাবেন না।

বর্তমান সঠিক উদাহরণ: `saree-04-sapphire-draped/`। নতুন mask `reference/saree-04-alpha-mask-GUIDE-ONLY.png`-এ; geometry `image 109.png`-এর mapped alpha থেকে নেওয়া, ছোট edge/lace noise পরিষ্কার করা হয়েছে। Source artwork, backgrounds এবং source lettering কপি করা হয়নি। নতুন ডেমোর RGB নয়, garment silhouette/cutout structure অনুসরণ করা হয়েছে।

`image 108.png`-এ আলাদা blouse band, diagonal pallu এবং narrow open waist আছে। `109` ও `110`-এ curved broad pallu, rounded neckline, পাশের বড় cutouts এবং lower-drape/foot openings আছে। 109/110 কাছাকাছি layout হলেও alpha pixel-for-pixel একই নয়। ভবিষ্যতের নতুন শাড়িতে 01–03-এর full-waist alpha নয়, এই নতুন cutout structure ভিত্তি হিসেবে নিন; প্রয়োজন হলে ব্যবহারকারীর নতুন reference অনুযায়ী বদলান।

আগের পূর্ণ torso/leg coverage সম্পর্কিত নিচের বর্ণনাগুলো প্রথম সংস্করণের ঐতিহাসিক নোট; সেগুলো নতুন ডিজাইনের শর্ত নয়।

## ব্যবহারকারীর বর্তমান নির্দেশ

- এখন পাঞ্জাবি নয়, শাড়ি তৈরি হবে।
- শাড়ি **Classic Pants**: ব্লাউজ, চওড়া আঁচল ও নিচের শাড়ি থাকবে; neckline, কোমর/মিডরিফ, উপযুক্ত পাশে এবং drape-এ cutouts থাকবে; দুই হাত খোলা থাকবে।
- প্রতিটি নতুন শাড়ির সঙ্গে matching short-sleeve Shirt দিতে হবে; অতিরিক্ত বালা বা অন্য হাতের কাজ শুধু আলাদা নির্দেশ থাকলে।
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

## প্রথম তৈরি শাড়ির alpha এবং placement — পুরোনো full-waist সংস্করণের ইতিহাস

- পুরোনো **পাঞ্জাবির neck/hand mask ব্যবহার করা হয়নি**। সেই mask-এ hand cutouts আছে; Pants-এ লাগালে তা পায়ের অংশ কেটে ফেলবে।
- `image 102.png`-এর upper/front torso neckline alpha 585×559-এ resample করে নেওয়া হয়েছে; torso neckline-এ y109 পর্যন্ত প্রয়োগ করা হয়েছে।
- UP ও FRONT-এর separator y72–73-এ adjacent neck alpha চালিয়ে দেওয়া হয়েছে, যাতে opening-এর মধ্যে অস্বাভাবিক রঙের bridge না থাকে।
- দুই পায়ের সব ছয়টি face পুরো opaque। Torso neckline ছাড়া বুক, কোমর এবং পায়ের কাপড় ঢাকা।
- Final alpha সংরক্ষিত `saree-01-ivory-crimson/reference/saree-01-neck-alpha-mask-GUIDE-ONLY.png`-এ। এটি alpha channel; কাপড়ের ওপর দৃশ্যমান ছবি হিসেবে বসাবেন না।
- Native borders-এর বাইরে প্রায় 1-pixel bleed আছে; unused canvas সাদা এবং `2.94` লেখা wearable faces-এর বাইরে।
- আঁচল front থেকে shoulder UP পেরিয়ে back-এ যায়। Front leg-এর দুই half-এ shallow curved band আছে; hem height চারপাশে একই।

## প্রতিটি শাড়ির সঙ্গে হাতার Shirt তৈরির নিয়ম

1. মূল Pants অক্ষত রাখুন।
2. নতুন **585×559 RGBA Classic Shirt** বানান।
3. Shirt-এর সব mapped torso face-এর alpha **0** রাখুন, নইলে তা Pants-এ আঁকা বুক ও আঁচল ঢেকে দিতে পারে।
4. Shirt-এর arm UP/FRONT/BACK/LEFT/RIGHT face-এ চাওয়া sleeve/bangle design বসান। Sample 103/107-এর ছোট upper-arm band না full sleeve—ব্যবহারকারীর নির্দেশ অনুযায়ী নির্বাচন করুন।
5. হাতের যে অংশ খোলা থাকবে সেখানে আসল alpha transparency দিন; skin-color বা checkerboard আঁকবেন না।
6. Pants-এর pallu/waist/leg continuity এবং Shirt-এর arm borders আলাদাভাবে পরীক্ষা করুন।
7. Preview file তৈরি করবেন না। Native PNG দেখে এবং torso composite-এর pixel comparison করে sleeve-এর কাজ যাচাই করুন।

## রপ্তানি ও যাচাই

একটি folds-সহ version, PNG/RGBA8, exact 585×559। Source sample branding, UV outline, visible masks, guide text, mannequin অথবা background wearable faces-এ নয়। Check neckline, blouse ও pallu-এর কাভারেজ, সত্যিকারের midriff/side transparency, leg drape openings, leg center join, pallu seam ও hem। সব leg face পুরো opaque থাকা বাধ্যতামূলক নয়; নতুন ডেমোতে intentional openings রয়েছে। Roblox Studio-তে পরীক্ষা না করলে সেভাবে পরীক্ষা হয়েছে বলে দাবি করবেন না।
