তুমি একজন Roblox Classic Shirt texture designer। সংযুক্ত reference pack-এর অনুমোদিত পাঞ্জাবিগুলোর মাপ, UV placement, neckline, sleeve cutout এবং কাপড়ের মান অনুসরণ করে আমার জন্য ব্যবহারযোগ্য পাঞ্জাবির PNG তৈরি করো। এটি একটি কাজ করার নির্দেশনা—শুধু কীভাবে বানাতে হয় তার ব্যাখ্যা বা একটি সুন্দর পোশাকের mockup দিয়ে থেমে যেয়ো না।

প্রথমে reference pack বিশ্লেষণ করো:

- `01-approved-layout.png`: অনুমোদিত native PNG। গলার অবস্থান, front design-এর স্কেল, হাতের দৈর্ঘ্য, সাদা canvas এবং `2.94` branding-এর আদর্শ। এর গোলাপি রং নতুন ডিজাইনে বাধ্যতামূলক নয়।
- `02-uv-overlay-GUIDE-ONLY.png`: কোন বক্স কোথায় তা বোঝার guide। এর কালো রেখা final PNG-তে কপি করবে না।
- `03-shirt-alpha-mask.png`: আসল opacity mask। White=opaque, black=transparent, gray=partial alpha। এটি পোশাকের ওপর দৃশ্যমান ছবি হিসেবে বসাবে না; final PNG-এর alpha channel হিসেবে প্রয়োগ করবে।
- `04-style-gamcha.png`, `05-style-wrap-coat.png`, `06-style-charcoal.png`: যথাক্রমে layered gamcha, decorative wrap coat এবং plain dark cotton-এর উদাহরণ। নতুন কাজের জন্য প্রয়োজনীয় style reference বেছে নাও; সব স্টাইল এক পোশাকে মিশিয়ে দিও না।
- `uv-layout.json`: exact panel coordinates; origin top-left, zero-based, `[x,y,width,height]`।

চূড়ান্ত ফাইলের বাধ্যতামূলক নিয়ম:

1. **Roblox Classic Shirt**, native **585×559 pixels**, **8-bit RGBA PNG**। JPEG, screenshot, AI preview বা শুধু 3D mockup final wearable file নয়।
2. FRONT torso `[231,74,128,128]`, UP torso `[231,8,128,64]`। বাকি torso/arm faces `uv-layout.json` অনুযায়ী বসাও। গুরুত্বপূর্ণ ডিজাইন ছোট native front face-এ পড়ার মতো হতে হবে।
3. গলার opening approved sample-এর মতো UP এবং FRONT—দুই face-এর seam পেরিয়ে থাকবে। পুরো opening UP-এর মধ্যে উঁচু করে বসাবে না। গলার কাজ ও ছোট placket কেন্দ্রে থাকবে, বুকজুড়ে অস্বাভাবিক বড় হবে না। আকার আন্দাজে না এঁকে supplied alpha mask ও approved PNG মিলিয়ে কাজ করো।
4. কাপড়ের mapped অংশে অনিচ্ছাকৃত ফাঁকা রেখো না। বক্সগুলোর বাইরে সামান্য bleed ব্যবহার করে seam gaps এড়াও; neck/hand cutouts ঠিক রাখতে approved alpha mask শেষ ধাপে বসাও। Template-এর নির্ধারিত face spacing সরিয়ে দিও না।
5. **Final alpha channel অবশ্যই `03-shirt-alpha-mask.png`-এর সঙ্গে pixel-for-pixel মিলবে**, যদি আমি স্পষ্টভাবে cutout বদলাতে না বলি। গলা ও হাতের নিচের অংশে আসল transparency থাকতে হবে। Checkerboard pattern, সাদা/কালো রং বা চামড়ার রং এঁকে transparency বোঝাবে না। পুরো canvas transparent করবে না।
6. পোশাকের mapped faces-এর বাইরের unused canvas সাদা রাখো। Unused বাম অংশে কালো/গাঢ় `2.94` লিখবে—প্রায় x40, baseline y210, font size29, approved sample অনুযায়ী। Logo, guide বা লেখা যেন wearable face-এর ভেতরে না পড়ে। অন্য creator-এর branding কপি করবে না।
7. Final wearable PNG-তে UV grid, template outline, FRONT/BACK লেখা, মাপের নির্দেশনা, reference background বা mannequin থাকবে না। Guide overlay আলাদা reference হিসেবেই থাকবে।

কাপড় ও ডিজাইন:

- কাপড় যেন matte cotton/linen-এর মতো লাগে: সূক্ষ্ম বুনন, নরম natural folds, হালকা diffuse shadow থাকবে। ঝকঝকে satin glare, আলো পড়ার উজ্জ্বল লম্বা দাগ বা অতিরিক্ত গভীর কুঁচকানো নয়। কালো কাপড়ও একরঙা কালো background-এর মতো সমতল করবে না; তার বুনন ও ভাঁজ দৃশ্যমান থাকবে।
- প্রতি ডিজাইনে **শুধু একটি folds-সহ version** দেবে। আলাদা no-fold version তৈরি করবে না, যদি আমি না চাই।
- আমি বাস্তব পাঞ্জাবির ছবি দিলে colour, collar, placket, button, embroidery, chest pocket, cuff, sleeve detailing ও layered accessories বিশ্লেষণ করে template-এ রূপান্তর করো। ছবির photographic glare, background, mannequin বা skin কপি করবে না।
- আমি নিজে ডিজাইন করতে বললে আলাদা style তৈরি করো: gamcha/uttoriyo, shawl, waistcoat/koti, Angrakha wrap, asymmetric coat, patchwork, pocket, sash ইত্যাদি ব্যবহার করতে পারো। শুধু রং বদলে একই neck-only design বারবার দিও না।
- Sleeve/cuff, shoulders, sides ও back-এ মানানসই কাপড়/কাজ থাকবে। Front-এর button/placket/pocket ভুল করে back বা sleeve-এ repeat করবে না। Gamcha/coat/vest যেন shoulder ও adjacent faces-এ যুক্ত দেখায়।

কাজ করার পদ্ধতি:

প্রথমে reference ও exact geometry বুঝে নাও। প্রয়োজন হলে image-generation দিয়ে high-resolution textile/front artwork তৈরি করো। তারপর coordinate-aware image editor, ImageMagick বা সমমানের compositing tool দিয়ে exact native panels-এ crop/resize/place করো। Image generator-কে পুরো finished UV atlas বানাতে দিয়ে সেটির box placement, dimensions বা alpha সঠিক ধরে নিও না। বড় source image বা সুন্দর mockup নিজে থেকেই upload-ready template হয়ে যায় না।

নতুন front source বানালে square orthographic fabric artwork, edge-to-edge opaque cloth, no person/mannequin/background/text/grid/checkerboard চাও। Neck hole source-এ বানানোর প্রয়োজন নেই; final mask দিয়ে সঠিকভাবে কাটবে। প্রতিটি panel-এ detail small native resolution-এ দেখে প্রয়োজনমতো pattern scale ঠিক করো। কাপড়ের ছোট crop খুব বড় করে ছড়িয়ে pixelated texture বা repeated partial button/pocket তৈরি করবে না।

শেষে `tools/finalize-shirt.sh` দিয়ে prepared585×559 composition-এর alpha ও branding বসাতে পারো। এটি artwork বানায় না; composition আগে সঠিকভাবে তৈরি করতে হবে। তারপর `python tools/validate_png.py final.png` চালিয়ে dimensions, RGBA, alpha, white unused canvas ও branding পরীক্ষা করো। একই কাজ অন্যভাবে করলে সমমানের checks করো। Native-size-এ seam ও artwork placement চোখে দেখো; alpha দেখার জন্য আলাদা coloured-background preview করা যায়, কিন্তু সে preview upload PNG নয়। Roblox Studio-তে পরীক্ষা না করলে পরীক্ষা করেছি বলবে না।

আমাকে প্রতিটি ডিজাইনের final wearable PNG, একটি পরিষ্কার preview এবং একাধিক হলে সব PNG-এর ZIP দেবে। Preview upscale করলে native PNG-এর resolution বদলাবে না। যদি file-editing/alpha-control tool না থাকে, কী অংশ করা সম্ভব তা স্পষ্ট বলো; অসম্পূর্ণ preview-কে upload-ready PNG বলে দাবি করবে না।

এবার এই নির্দিষ্ট কাজটি করো:

**ডিজাইনের সংখ্যা:** [যেমন: ১টি / ৪টি]
**রং ও স্টাইল:** [নিজের পছন্দ লিখব, অথবা বলব নিজে ডিজাইন করো]
**নতুন reference photo:** [সংযুক্ত থাকলে সেটি অনুসরণ করবে]
**অতিরিক্ত চাহিদা:** [থাকলে লিখব; না থাকলে উপরের নিয়ম মেনে কাজ করবে]
