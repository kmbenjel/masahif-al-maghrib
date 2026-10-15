# فيديو تعريفي: مصاحف المغرب

مقطعان قصيران عموديان (1080×1920، نحو 71 ثانية) للتعريف بموقع
[masahif-al-maghrib.com](https://masahif-al-maghrib.com/)، يصلحان للنشر في
إنستغرام وتيك توك ويوتيوب شورتس وفيسبوك وواتساب: واحد بالعربية وآخر بالإنجليزية.

| الملف | الاستعمال |
|---|---|
| `out/masahif-al-maghrib-ar.mp4` | النسخة العربية بالجودة الكاملة، للرفع على المنصات |
| `out/masahif-al-maghrib-en.mp4` | النسخة الإنجليزية بالجودة الكاملة |
| `out/masahif-al-maghrib-ar-whatsapp.mp4` | نسخة عربية خفيفة (720p) للإرسال في واتساب وتلغرام |
| `out/masahif-al-maghrib-en-whatsapp.mp4` | نسخة إنجليزية خفيفة |
| `out/cover-ar.jpg` و`out/cover-en.jpg` | صورة غلاف للمنصات التي تطلبها (لحظة ظهور اسم الموقع) |

## المحتوى

1. **مدخل**: مصحف بخط سلطان المغرب في المسجد الأقصى، وآخر من خزانة المنصور الذهبي في إسبانيا، وثالث في ميونخ.
2. **الكرة الأرضية**: من فاس إلى مكتبات العالم التي تحفظ اليوم مصاحف الدليل، ثم يظهر اسم الموقع.
3. **العصور**: اثنا عشر قرناً، سبعة عصور، أكثر من ستين مصحفاً، على خط زمني بألوان العصور في الموقع نفسه.
4. **نفائس**: ربعتا المرتضى وأبي الحسن بخط يديهما، وخاتمة مصحف المنصور بالذهب على اللازورد، والمصحف الأخضر.
5. **الموقع على الهاتف**: بطاقة مصحف أبي يعقوب يوسف، والعارض المقرِّب، وروابط النسخ المرقمنة (لقطات حقيقية من الموقع).
6. **المُعِدّ**: إبراهيم حسني إدريسي، الخطاط والباحث في المخطوطات، أستاذ الخطوط المغربية بفاس.
7. **الدعوة**: دليل موثق بالعربية والإنجليزية، ثم عنوان الموقع يُكتب حرفاً حرفاً.
8. **الختام**: «تطوير الموقع وإنتاج الفيديو: خالد بن جلون، مطوّر من فاس».

عنوان الموقع ظاهر أعلى الإطار طوال المقطع، والتعليق الصوتي مكتوب أسفله كلمةً كلمة لمن يشاهد بلا صوت.

**الصوت**: صوت «حامد» (ar-SA-HamedNeural) للعربية، و«أندرو» (en-US-AndrewNeural) للإنجليزية، من أصوات مايكروسوفت العصبية.
تحققنا من نطق كل جملة، ومنها عنوان الموقع والأسماء، بتفريغها آلياً (Whisper) ومقارنتها بالنص.
وليس في المقطع موسيقى، احتراماً لموضوعه؛ وفيه مؤثرات خفيفة مولّدة (انتقالات، ونقرات الكتابة، ورنة خفيفة عند ظهور الاسم).

## إعادة الإنتاج

كل إطار دالة في الزمن وحده: المشهد صفحة HTML (`scene/`) تُرسم بالزمن `t`، ويلتقطها Chromium إطاراً إطاراً.

```bash
pip install edge-tts numpy scipy soundfile        # والأدوات: ffmpeg وImageMagick وNode مع Playwright
python tools/tts.py ar && python tools/tts.py en              # التعليق الصوتي وتوقيت كل كلمة
python tools/build_timeline.py ar && python tools/build_timeline.py en
tools/prep_images.sh                                           # خلفيات مموهة
node tools/capture_ui.js                                       # لقطات الموقع على الهاتف
node tools/render.js ar 3 && python tools/mix.py ar && tools/encode.sh ar
node tools/render.js en 3 && python tools/mix.py en && tools/encode.sh en
```

لتعديل النص: `voice/script.<lang>.json` (الحقل `say` لما يُنطق و`show` لما يُكتب إن اختلفا)،
ثم أعد توليد الصوت والخط الزمني. ونصوص الشاشة والصور ونقاط التزامن في `scene/content.js`.
ولمعاينة لحظة بعينها: `node tools/stills.js ar 12.5 30` أو افتح `scene/index.html?lang=ar&play` على خادم من جذر الموقع.

## المصادر والتراخيص

- صور المصاحف من الموقع نفسه، ومصادرها مذكورة تحت كل صورة فيه. وصورتا خاتمة مصحف المنصور (`assets/`)
  مأخوذتان من عارض IIIF للتراث الوطني الإسباني (Patrimonio Nacional)، الإسكوريال، árabe 1340، الورقة 264و، كما يفعل الموقع.
- الخطوط: أميري وIBM Plex Sans Arabic من الموقع، وNoto Kufi Arabic وSource Serif 4 وIBM Plex Sans من @fontsource (رخصة SIL OFL).
- الخريطة: Natural Earth عبر world-atlas (ملك عام / ISC)، والمغرب مرسوم بصحرائه شكلاً واحداً بلا حد داخلي. وd3-geo وtopojson-client (ISC).

---

# Promo video: Masahif al-Maghrib

Two short vertical cuts (1080×1920, about 71 s) introducing
[masahif-al-maghrib.com](https://masahif-al-maghrib.com/), one in Arabic and one in English,
for Reels, Shorts, TikTok, Facebook and WhatsApp. The files are in `out/` (full quality, and a
lighter 720p copy for messaging apps). The narration (Microsoft neural voices Hamed and Andrew)
was checked line by line with Whisper, the URL and the names included. There is no music, out of
respect for the subject, only light synthesized sound effects. The commands above rebuild
everything: `scene/` is an HTML page drawn as a pure function of time and captured frame by
frame with Chromium. Credits: “Website development & video production: Khalid Benjelloun,
developer from Fez.”
