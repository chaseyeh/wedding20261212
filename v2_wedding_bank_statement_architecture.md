# 囍事銀行電子喜帖 V2 — 網頁開發規格

> 專案名稱：HESU BANK｜永軒 × 昀蓁 終身聯名帳戶  
> 婚禮日期：2026.12.12  
> LINE 官方帳號：@634ydtgf  
> 主要入口：LINE 官方帳號圖文選單  
> 預計網站：`https://chaseyeh.github.io/wedding20261212/`

---

## 1. V2 改版目標

第二版網站不再只是「銀行對帳單風格的婚禮網頁」，而是要完整串接 LINE 圖文選單，形成一套一致的婚禮數位體驗。

核心概念：

**LINE 是入口、網站是主體、HESU BANK 是整體世界觀。**

賓客從 LINE 圖文選單點擊後，可直接進入網站不同區塊：

- 電子喜帖 → 網站首頁
- 出席回覆 → RSVP 區塊
- 交通指南 → Location 區塊
- 絕美婚紗 → Gallery 區塊

網站所有功能都集中在同一個 `index.html`，使用 Anchor 導航，不建立多個獨立頁面。

---

# 2. LINE 圖文選單對應架構

目前圖文選單結構：

```text
┌─────────────────────────────────────┐
│                                     │
│          永軒 & 昀蓁                │
│          WEDDING                    │
│          2026.12.12                 │
│                                     │
│             電子喜帖 ＞             │
│                                     │
├────────────┬────────────┬───────────┤
│            │            │           │
│  出席回覆  │  交通指南  │  絕美婚紗 │
│     ＞     │     ＞     │     ＞    │
└────────────┴────────────┴───────────┘
```

對應網址：

```text
電子喜帖
https://chaseyeh.github.io/wedding20261212/

出席回覆
https://chaseyeh.github.io/wedding20261212/#rsvp

交通指南
<!-- https://chaseyeh.github.io/wedding20261212/#location -->
https://www.google.com/maps/search/?api=1&query=%E6%B8%85%E6%96%B0%E6%BA%AB%E6%B3%89%E9%A3%AF%E5%BA%97%20%E5%8F%B0%E4%B8%AD%E5%B8%82%E7%83%8F%E6%97%A5%E5%8D%80%E6%BA%AB%E6%B3%89%E8%B7%AF2%E8%99%9F

絕美婚紗
https://chaseyeh.github.io/wedding20261212/#gallery
```

若之後部署網域改變，只需修改 Base URL。

---

# 3. 整體資訊架構

```text
LINE Official Account
│
├── Rich Menu
│   │
│   ├── 電子喜帖 ───────→ /
│   │
│   ├── 出席回覆 ───────→ /#rsvp
│   │
│   ├── 交通指南 ───────→ /#location
│   │
│   └── 絕美婚紗 ───────→ /#gallery
│
├── AI 婚禮小管家
│   ├── 婚宴時間
│   ├── 婚宴地點
│   ├── 交通資訊
│   ├── 出席修改
│   └── 婚禮 FAQ
│
└── HESU BANK Wedding Website
    │
    ├── 01 Cover
    ├── 02 Account Overview
    ├── 03 Statement Summary
    ├── 04 Transaction History
    ├── 05 Asset Portfolio / Gallery
    ├── 06 Branch Information / Location
    ├── 07 Attendance Confirmation / RSVP
    ├── 08 LINE Wedding Assistant
    └── 09 Print Statement
```

---

# 4. 設計方向

## 4.1 整體風格

網站需融合三種視覺語言：

1. **HESU BANK 銀行對帳單**
2. **韓系婚禮插畫**
3. **中式婚禮元素**

避免網站變成純黑白金融文件，也避免完全變成傳統紅色喜帖。

目標風格：

> 中式婚禮 × 韓系插畫 × Banking Editorial

---

## 4.2 與 LINE 圖文選單的視覺連續性

LINE 圖文選單已有以下元素：

- 米白底色
- 暖紅／珊瑚紅
- 深棕中文字
- 淺綠植物
- 牡丹花
- 雙囍
- 新人似顏繪
- 手繪感
- 圓角卡片
- 柔和紙張質感

網站 V2 必須延續這些元素。

銀行元素則以「資訊排版」呈現，而不是冷硬金融 UI。

可使用：

- Statement 編號
- Account No.
- 細線表格
- Receipt / Statement 標籤
- 印章
- 帳戶狀態
- Transaction Row
- Barcode / Serial Number 裝飾
- 虛線裁切感
- 紙張邊框

---

# 5. 建議 Design Tokens

以下色碼為設計建議，可再依實際插畫調整。

```css
:root {
  --color-bg: #FFF9F1;
  --color-paper: #FFFDF8;

  --color-red: #C95043;
  --color-red-soft: #E98D7C;
  --color-red-light: #F7D7CF;

  --color-brown: #62382B;
  --color-brown-light: #9C6A58;

  --color-green: #7B8B68;
  --color-green-light: #DCE3D4;

  --color-gold: #B88852;

  --color-border: #D7B7A3;
  --color-text: #4A3029;
  --color-muted: #94776D;
}
```

---

# 6. 字體建議

中文字體：

```text
Noto Serif TC
LXGW WenKai TC
jf open 粉圓
思源宋體
```

英文／數字：

```text
Cormorant Garamond
Libre Baskerville
DM Serif Display
Inter
```

設計原則：

- 中文標題可以偏手寫／宋體
- 銀行資訊、日期、Statement 編號使用 Serif 或 Monospace
- 正文以易讀為優先

---

# 7. 網站 Section 架構

---

## 01 — COVER

### ID

```html
<section id="home">
```

### 目的

第一屏建立 HESU BANK 世界觀。

### 內容

```text
HESU BANK

JOINT ACCOUNT
STATEMENT

Account Holders
永軒 × 昀蓁

Statement Date
2026.12.12

Account Status
FOREVER ACTIVE
```

主視覺使用：

- 新人婚紗照
或
- 與 LINE 圖文選單相同風格的新人似顏繪

CTA：

```text
VIEW STATEMENT
查看喜帖 ↓
```

### UX

手機載入後必須在 1 個畫面內看到：

- 新人名字
- 日期
- HESU BANK
- CTA

---

# 8. 02 — ACCOUNT OVERVIEW

### ID

```html
<section id="overview">
```

### 標題

```text
02
ACCOUNT OVERVIEW
帳戶總覽
```

### 基本資料

```text
Account Holders
永軒 × 昀蓁

Account Type
Lifetime Joint Account
終身聯名帳戶

Opening Date
2026.12.12

Account Status
ACTIVE / FOREVER
```

---

## LOVE PORTFOLIO

以銀行資產配置呈現兩人的生活。

範例：

```text
一起吃飯          28%
互相吐槽          22%
旅行              18%
陪伴              15%
包容              10%
浪漫               5%
誰去倒垃圾         2%
```

視覺可使用：

- 水平比例條
- Statement row
- 小型圓餅圖，中央標示「幸福資產現值 ∞」
- 純文字百分比

避免使用過度商業 Dashboard。

---

# 9. 03 — STATEMENT SUMMARY

### ID

```html
<section id="wedding-info">
```

### 標題

```text
03
STATEMENT SUMMARY
婚禮帳戶摘要
```

### 婚禮資訊

```text
Transaction Date
2026.12.12 SAT.

Welcome
11:30

Wedding Banquet
12:00

Merchant
清新溫泉飯店

Address
台中市烏日區溫泉路 2 號
```

---

## AMOUNT DUE 趣味欄位

```text
AMOUNT DUE

一份祝福
＋
一顆準時抵達的心
```

---

## CTA

```text
加入行事曆
查看交通
```

加入行事曆功能需由 JavaScript 產生 `.ics`。

---

# 10. 04 — TRANSACTION HISTORY

### ID

```html
<section id="story">
```

### 標題

```text
04
TRANSACTION HISTORY
愛情交易紀錄
```

以銀行流水帳呈現戀愛故事。

格式：

```text
DATE          DESCRIPTION               CREDIT

20XX.XX       FIRST MEETING             +1 HEART
20XX.XX       FIRST DATE                +1 MEMORY
20XX.XX       FIRST TRIP                +∞ HAPPINESS
20XX.XX       PROPOSAL                  +1 FIANCÉE
2026.12.12    MARRIAGE                  FOREVER
```

實際年份之後可再填入。

手機版可改成卡片式：

```text
2026.12.12
MARRIAGE

STATUS
FOREVER
```

---

# 11. 05 — ASSET PORTFOLIO

### ID

```html
<section id="gallery">
```

此 Anchor 必須保留，供 LINE 圖文選單直接跳轉。

### 標題

```text
05
ASSET PORTFOLIO
珍藏資產
```

副標：

```text
OUR MOST VALUABLE ASSETS
```

內容：

- 婚紗照 6～12 張
- Mobile 使用單欄／雙欄混排
- Desktop 可使用 Editorial Grid

點擊照片：

```text
Lightbox
```

需支援：

- 左右滑動
- ESC 關閉
- 手機觸控

不要自動播放 Carousel。

---

# 12. 06 — BRANCH INFORMATION

### ID

```html
<section id="location">
```

此 Anchor 必須保留。

### 標題

```text
06
BRANCH INFORMATION
宴會據點
```

內容：

```text
HESU BANK
TAICHUNG BRANCH

清新溫泉飯店
台中市烏日區溫泉路 2 號

2026.12.12

WELCOME
11:30

BANQUET
12:00
```

---

## CTA

```text
Google Maps
開啟導航
```

Google Maps 按鈕直接開啟飯店位置。

建議另外保留區塊：

```text
PARKING
停車資訊

TRANSPORTATION
交通方式
```

內容之後可再補。

---

# 13. 07 — ATTENDANCE CONFIRMATION

### ID

```html
<section id="rsvp">
```

此 Anchor 必須保留。

### 標題

```text
07
ATTENDANCE CONFIRMATION
出席回覆
```

可加入銀行語言：

```text
ACCOUNT AUTHORIZATION
出席授權確認
```

---

## RSVP 表單欄位

### 姓名／稱呼

```text
您的稱呼
```

Required。

### 出席狀態

```text
欣然出席
遺憾無法出席
```

Radio Button。

### 出席人數

```text
-   1   +
```

建議：

- 最小 1
- 最大 10

若選「無法出席」，人數自動變為 0。

### 兒童椅數量

選填，可選擇不需要或 1 至 10 張；確認回覆時會一併帶入訊息。

### 飲食

```text
葷食
素食
其他
```

Optional。

### 備註

```text
想告訴新人的話
```

Optional。

---

# 14. RSVP LINE 回覆流程

網站不建立資料庫。

使用者按：

```text
CONFIRM TRANSACTION
確認回覆
```

JavaScript 根據表單內容產生 LINE 預填訊息。

範例：

```text
您好，我是王小明。

2026/12/12 永軒與昀蓁婚宴出席回覆：

出席狀況：欣然出席
出席人數：2 位
兒童椅數量：1 張
飲食需求：葷食 1、素食 1

祝福你們新婚快樂！
```

流程：

```text
填寫 RSVP
↓
建立文字
↓
顯示確認畫面
↓
開啟 LINE
↓
賓客自行按下傳送
```

若 LINE 無法開啟：

```text
複製回覆內容
```

網站不儲存任何賓客資料。

---

# 15. LINE 官方帳號

官方帳號：

```text
@634ydtgf
```

請在 JavaScript 建立：

```js
const LINE_OFFICIAL_ACCOUNT_ID = "@634ydtgf";
```

實際 LINE 加好友 URL 或 LINE Share URL 請做成 Config，不要散落在程式中。

範例：

```js
const CONFIG = {
  lineOfficialAccountId: "@634ydtgf",
  lineOfficialAccountUrl: "",
  weddingDate: "2026-12-12",
  venue: "清新溫泉飯店"
};
```

---

# 16. 08 — LINE WEDDING ASSISTANT

### ID

```html
<section id="assistant">
```

### 標題

```text
08
CUSTOMER SERVICE
婚禮小管家
```

文案：

```text
還有問題嗎？

婚宴時間、交通、停車、
出席修改等問題，
都可以直接詢問 LINE 婚禮小管家。
```

CTA：

```text
OPEN LINE
詢問婚禮小管家
```

此區不必真的在網站內嵌 AI Chat。

AI 功能留在 LINE 官方帳號內。

---

# 17. 09 — PRINT STATEMENT

### ID

```html
<section id="print">
```

### 標題

```text
09
STATEMENT COPY
收藏這份喜帖
```

按鈕：

```text
PRINT / SAVE PDF
列印 / 儲存 PDF
```

JavaScript：

```js
window.print();
```

---

# 18. A4 列印版需求

必須建立：

```css
@media print
```

列印時：

### 隱藏

- Sticky Navigation
- CTA Button
- Gallery Lightbox
- LINE Button
- 動畫
- Scroll hint

### 顯示

- HESU BANK
- 新人姓名
- 日期
- 婚宴資訊
- 地址
- 戀愛故事
- 精選婚紗
- QR Code
- LINE ID

紙張：

```text
A4 Portrait
```

Margin：

```css
@page {
  size: A4;
  margin: 12mm;
}
```

列印結果必須看起來像：

> HESU BANK Wedding Account Statement

而不是單純把手機網站印出來。

---

# 19. Mobile First

主要使用情境：

```text
LINE
↓
LINE In-App Browser
↓
手機瀏覽
```

因此開發順序必須為：

```text
Mobile
↓
Tablet
↓
Desktop
↓
Print
```

Mobile breakpoint：

```css
@media (min-width: 768px)
```

Desktop：

```css
@media (min-width: 1024px)
```

---

# 20. Anchor 跳轉 UX

由 LINE 圖文選單進入：

```text
/#rsvp
/#location
/#gallery
```

頁面載入後必須：

1. 正確定位 Anchor
2. 考慮 Sticky Header 高度
3. 使用 `scroll-margin-top`
4. 不要被載入動畫阻擋

CSS：

```css
section {
  scroll-margin-top: 80px;
}
```

---

# 21. Navigation

手機版建議不要使用大型 Hamburger Menu。

可以使用簡單 Sticky Bar：

```text
喜帖
婚宴
婚紗
交通
回覆
```

或底部 Floating Navigation。

但整體不可搶過 LINE 圖文選單角色。

Navigation 主要是網站內瀏覽輔助。

---

# 22. 動畫

動畫需柔和。

可使用：

```text
fade-up
fade-in
line draw
number reveal
```

避免：

- 大量 Parallax
- 3D 動畫
- 自動播放影音
- 過度縮放
- 影響閱讀的 Scroll Hijacking

支援：

```css
@media (prefers-reduced-motion: reduce)
```

---

# 23. Accessibility

必須：

- 所有圖片加入 `alt`
- Button 可用鍵盤操作
- Form Label 正確綁定
- Focus State 清楚
- 顏色對比足夠
- 不只靠顏色辨識 RSVP 狀態
- Lightbox 可用 ESC 關閉

---

# 24. SEO / Social Share

`<head>` 需包含：

```html
<title>永軒 & 昀蓁｜2026.12.12 Wedding</title>
```

Description：

```text
永軒與昀蓁的婚禮電子喜帖。
2026 年 12 月 12 日，
誠摯邀請您一起見證我們的重要時刻。
```

Open Graph：

```text
og:title
og:description
og:image
og:url
og:type
```

分享 LINE 時需顯示漂亮的縮圖。

---

# 25. 建議專案結構

```text
wedding20261212/
│
├── index.html
│
├── README.md
│
│
├── assets/
│   │
│   ├── css/
│   │   ├── style.css
│   │   └── print.css
│   │
│   ├── js/
│   │   └── main.js
│   │
│   ├── images/
│   │   ├── hero/
│   │   ├── gallery/
│   │   ├── illustration/
│   │   └── icons/
│   │
│   └── fonts/
│
└── docs/
    └── v2_wedding_bank_statement_architecture.md
```

若不需要自訂字型，可移除 `fonts/`。

---

# 26. HTML Section 建議

```html
<body>

<header>
  Navigation
</header>

<main>

  <section id="home">
    Cover
  </section>

  <section id="overview">
    Account Overview
  </section>

  <section id="wedding-info">
    Statement Summary
  </section>

  <section id="story">
    Transaction History
  </section>

  <section id="gallery">
    Asset Portfolio
  </section>

  <section id="location">
    Branch Information
  </section>

  <section id="rsvp">
    Attendance Confirmation
  </section>

  <section id="assistant">
    LINE Wedding Assistant
  </section>

  <section id="print">
    Print Statement
  </section>

</main>

<footer>
  HESU BANK
  永軒 × 昀蓁
  2026.12.12
</footer>

</body>
```

---

# 27. JavaScript 功能清單

`assets/js/main.js`

需負責：

```text
01 Anchor smooth scroll
02 RSVP 人數加減
03 RSVP 狀態切換
04 LINE 訊息產生
05 複製 RSVP 文字
06 開啟 LINE
07 加入 Google Calendar / ICS
08 Gallery Lightbox
09 Print
10 Reduced Motion
```

不要加入 Framework。

使用：

```text
Vanilla HTML
Vanilla CSS
Vanilla JavaScript
```

專案需可直接部署至 GitHub Pages。

---

# 28. 不使用後端

V2 仍維持：

```text
No Database
No Backend
No Build Tool
```

避免：

```text
Node.js
React
Vue
Firebase
Supabase
PHP
Server API
```

除非未來另行要求。

---

# 29. Performance

目標：

```text
Lighthouse Performance > 90
Accessibility > 90
Best Practices > 90
SEO > 90
```

圖片：

- 使用 WebP / AVIF
- `loading="lazy"`
- Hero 圖片除外
- 圖片尺寸需指定 width / height
- 避免 CLS

---

# 30. Gallery 圖片策略

Hero：

```text
1 張
```

首頁／故事：

```text
2～3 張
```

Gallery：

```text
6～12 張
```

手機不應一次載入過大的原始婚紗 JPG。

建議：

```text
thumbnail
medium
original
```

或使用：

```html
srcset
```

---

# 31. 圖文選單與網站 Branding

LINE：

```text
溫暖
可愛
插畫
婚禮
```

網站：

```text
精緻
Editorial
銀行 Statement
收藏感
```

兩者共同 DNA：

```text
米白
暖紅
深棕
鼠尾草綠
牡丹
雙囍
新人插畫
圓角
紙張質感
```

因此使用者從 LINE 點入網站後不應感覺跳到另一套品牌。

---

# 32. 文案 Tone

不要使用正式金融機構的冰冷語氣。

應使用：

```text
銀行專有名詞
+
婚禮幽默
+
溫暖情感
```

例如：

```text
Account Type
終身聯名帳戶
```

```text
Account Status
FOREVER ACTIVE
```

```text
AMOUNT DUE
一份祝福＋一顆準時抵達的心
```

```text
Our Most Valuable Assets
我們最珍貴的資產
```

```text
本帳戶無到期日。
```

```text
本聯名帳戶自 2026.12.12 正式生效。
```

```text
存入日常，提領幸福。
```

---

# 33. 建議 Hero 文案

主版：

```text
HESU BANK

永軒 × 昀蓁

JOINT ACCOUNT STATEMENT

2026.12.12

兩個獨立帳戶，
自這一天起正式合併。

FOREVER ACTIVE
```

---

# 34. Footer 文案

```text
HESU BANK

YUNG-HSUAN × YUN-CHEN
2026.12.12

THANK YOU FOR BEING PART
OF OUR MOST IMPORTANT TRANSACTION.

存入日常，提領幸福。
```

---

# 35. V2 開發優先順序

### Phase 1

完成：

- HTML Section
- Anchor
- Mobile Layout
- HESU BANK 視覺

### Phase 2

完成：

- Gallery
- Location
- RSVP

### Phase 3

完成：

- LINE 串接
- ICS
- Print

### Phase 4

完成：

- 動畫
- SEO
- Performance
- Accessibility

---

# 36. 驗收條件

V2 完成後必須符合以下條件。

### LINE

- 電子喜帖可正確開首頁
- 出席回覆可直接定位 RSVP
- 交通指南可直接定位 Location
- 絕美婚紗可直接定位 Gallery

### Mobile

- LINE App 內瀏覽正常
- 無橫向捲動
- Button 至少 44px 高
- RSVP 可單手操作

### RSVP

- 必填欄位驗證
- 出席人數正確
- LINE 訊息正確
- 可複製訊息
- 網站不儲存資料

### Gallery

- 圖片可開啟
- 手機可滑動
- ESC 可關閉
- 圖片 Lazy Load

### Print

- A4 排版正常
- 不列印 Navigation
- 不列印互動按鈕
- 婚宴資料完整
- QR Code 可掃描

### Desktop

- 最大內容寬度控制
- 不因螢幕太寬而失去 Statement 感

---

# 37. Coding AI 開發指令

可將以下內容直接交給 Coding AI：

```text
請依照 v2_wedding_bank_statement_architecture.md，
重新製作 HESU BANK 婚禮電子喜帖 V2。

技術限制：
- Vanilla HTML
- Vanilla CSS
- Vanilla JavaScript
- 不使用 Framework
- 不使用 Backend
- 可直接部署 GitHub Pages

主要入口來自 LINE 官方帳號圖文選單。

必須支援：
/
/#rsvp
/#location
/#gallery

設計風格：
中式婚禮 × 韓系插畫 × Banking Editorial

色彩需延續 LINE 圖文選單：
米白、暖紅、深棕、鼠尾草綠。

網站主題：
HESU BANK
永軒 × 昀蓁
Lifetime Joint Account
2026.12.12

請優先完成 Mobile 版，
並確保 LINE In-App Browser 可正常使用。

請保留現有 RSVP 使用 LINE 預填訊息完成回覆的邏輯，
網站不得儲存賓客資料。

最後請提供：
1. index.html
2. assets/css/style.css
3. assets/css/print.css
4. assets/js/main.js
5. README.md
```

---

# 38. V2 最終體驗

理想使用流程：

```text
賓客收到 LINE
↓
看到圖文選單
↓
電子喜帖
↓
HESU BANK Cover
↓
婚宴資訊
↓
愛情交易紀錄
↓
婚紗照片
↓
交通
↓
出席回覆
↓
開啟 LINE
↓
送出 RSVP
```

如果賓客第二次進入：

```text
LINE
↓
直接點「出席回覆」
↓
#rsvp
```

或：

```text
LINE
↓
交通指南
↓
#location
```

不需要重新瀏覽整份喜帖。

---

# 39. 核心設計原則

V2 不只是：

> 一個銀行風格的婚禮網站

而應該是：

> 一份可以閱讀、互動、收藏，
> 並透過 LINE 完成婚禮服務的
> HESU BANK 終身聯名帳戶對帳單。

網站負責：

```text
資訊
情感
視覺
互動
```

LINE 負責：

```text
入口
通知
問答
出席確認
```

兩者共同形成：

# HESU BANK Wedding Experience

**永軒 × 昀蓁**  
**2026.12.12**
