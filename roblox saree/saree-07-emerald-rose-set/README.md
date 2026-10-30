# শাড়ি ০৭ — Emerald / Rose, আলাদা Pants ও হাতার Shirt

একটি matched set, **দুটি আলাদা 585×559 RGBA8 PNG**:

| ফাইল | Roblox asset type | কাজ |
| --- | --- | --- |
| `saree-07-emerald-rose-pants.png` | **Classic Pants** | পান্না-সবুজ শাড়ি, গোলাপি-মেরুন cropped blouse, চওড়া আঁচল ও নিচের শাড়ি |
| `saree-07-rose-sleeves-shirt.png` | **Classic Shirt** | শুধু matching ছোট ব্লাউজের হাতা; সব mapped torso face transparent |

## একসঙ্গে ব্যবহার

1. শাড়ির PNG **Classic Pants** হিসেবে upload/লাগান।
2. হাতার PNG **Classic Shirt** হিসেবে upload/লাগান।
3. দুটো একসঙ্গে পরলে matching short sleeves যোগ হবে। শুধু Pants পরলে হাত আগের মতো খোলা থাকবে।

এটি square front-only T-shirt graphic নয়। হাতা wrap করার জন্য native Classic Shirt template ব্যবহার করা হয়েছে।

## নতুন ডিজাইন

Emerald saree ও deeper-green curved pallu-তে antique-gold paisley embroidery। Rose-fuchsia blouse ও matching sleeves-এ ছোট gold dotwork। হাতার কিনারায় emerald band ও সরু সোনালি vine। কাপড়ের ভাঁজ নরম, low-contrast। শাড়ির neckline, side, midriff ও lower-drape openings অনুমোদিত শাড়ি ০৪-এর mask অনুযায়ী আছে।

## ডেমো পর্যবেক্ষণ

ব্যবহারকারীর `saree hand.zip`-এ `image 103.png` ও `image 107.png` আছে। দুটোই 586×559 RGBA reference; তাই সরাসরি upload file হিসেবে কপি/resize করা হয়নি। Native 585×559 panel coordinates-এ নতুন artwork পুনর্গঠন করা হয়েছে।

মূল mapped torso faces transparent; 103-এর arm-side artwork প্রায় y355–403 এবং 107-এর প্রায় y355–410 পর্যন্ত। অর্থাৎ top arm cap ও বাহুর ওপরের অংশে কাপড়; নিচে forearm/hand খোলা। নতুন সেটে দ্বিতীয়টির মতো প্রায় 56 native pixels লম্বা short sleeves রাখা হয়েছে। Sample-এর background, branding বা RGB artwork কপি করা হয়নি।

বিশেষভাবে **Shirt-এর torso UP, FRONT, BACK, LEFT, RIGHT ও DOWN—সব face-এর alpha 0**। Sample branding যেখানে torso DOWN-এর মধ্যে পড়ে সেটিও নতুন Shirt-এ রাখা হয়নি। তাই Shirt শাড়ির বুক/আঁচল বা কোমরের খোলা অংশ ঢাকে না।

## প্রিভিউ ও ZIP

- `saree-07-with-sleeves-preview.png`: পুরো matched set-এর সামনে-পেছন।
- `saree-07-pants-only-preview.png`: শুধু শাড়ি, হাতা ছাড়া।
- `saree-07-layer-comparison.png`: শুধু Pants বনাম Pants + Shirt, পাশাপাশি front views।
- `saree-07-pants-and-sleeves.zip`: দুইটি wearable native PNG একসঙ্গে।
- `pants-uv-layout.json` ও `outfit-uv-layout.json`: geometry ও পৃথক file roles।

যাচাই: উভয় PNG-র exact 585×559/RGBA8, শাড়ির approved alpha, Shirt-এর সব mapped torso pixel alpha 0, opaque upper-arm caps, প্রায় 56-pixel short sleeves, transparent lower arms/hands। Pants-এর ওপর Shirt composite করেও torso artwork ও alpha pixel-for-pixel অপরিবর্তিত থাকে। ZIP integrity এবং preview-ও পরীক্ষা করা হয়েছে। Roblox Studio-তে পরীক্ষা করা হয়নি।

স্থায়ী reference notes: [SAREE-RESEARCH.md](../SAREE-RESEARCH.md)। ভবিষ্যতে শুধু শাড়ি চাইলে unique Pants তৈরি হবে; হাতা চাইলে তার জন্য আলাদা matching Shirt PNG দিতে হবে।
