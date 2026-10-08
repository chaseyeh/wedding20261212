from pathlib import Path
import tempfile

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
INVITES = ROOT / "invatation_zh"
OUTPUT = ROOT / "HESUBANK-wedding-statement.pdf"
PREVIEW = Path(tempfile.gettempdir()) / "hesubank-statement-preview.png"

DPI = 300
WIDTH = round(210 * DPI / 25.4)
HEIGHT = round(297 * DPI / 25.4)
LEFT = 148
RIGHT = WIDTH - LEFT
CONTENT = RIGHT - LEFT

# Sampled from the approved invitation: warm paper, ink black, and cinnabar.
PAPER = (241, 231, 222)
PANEL = (247, 241, 234)
INK = (45, 42, 38)
MUTED = (112, 99, 89)
LINE = (198, 169, 151)
LINE_SOFT = (218, 199, 184)
RED = (157, 44, 34)
RED_SOFT = (181, 75, 52)

FONT_SANS = r"C:\Windows\Fonts\msyh.ttc"
FONT_SERIF = r"C:\Windows\Fonts\simsun.ttc"
FONT_LATIN = r"C:\Windows\Fonts\georgia.ttf"
FONT_LATIN_BOLD = r"C:\Windows\Fonts\georgiab.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


canvas = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
draw = ImageDraw.Draw(canvas)

f_mark = font(FONT_SERIF, 78)
f_bank = font(FONT_SERIF, 48)
f_english = font(FONT_LATIN, 26)
f_english_bold = font(FONT_LATIN_BOLD, 27)
f_tiny = font(FONT_LATIN, 23)
f_eyebrow = font(FONT_LATIN, 27)
f_name = font(FONT_SERIF, 112)
f_amp = font(FONT_LATIN, 72)
f_subtitle = font(FONT_SERIF, 35)
f_notice = font(FONT_SERIF, 32)
f_notice_small = font(FONT_LATIN, 24)
f_section = font(FONT_SERIF, 43)
f_section_en = font(FONT_LATIN, 24)
f_asset = font(FONT_SERIF, 36)
f_asset_en = font(FONT_LATIN, 22)
f_percent = font(FONT_LATIN_BOLD, 47)
f_detail_label = font(FONT_LATIN, 23)
f_detail_value = font(FONT_SERIF, 40)
f_detail_small = font(FONT_SANS, 25)
f_footer = font(FONT_SERIF, 26)
f_footer_en = font(FONT_LATIN, 21)


def text(x, y, value, face, color=INK, anchor="lt"):
    draw.text((int(x), int(y)), value, font=face, fill=color, anchor=anchor)


def tracked(x, y, value, face, color, spacing=3):
    cursor = x
    for character in value:
        text(cursor, y, character, face, color)
        cursor += draw.textlength(character, font=face) + spacing
    return cursor


def rule(y, color=LINE, width=3, x1=LEFT, x2=RIGHT):
    draw.line((x1, y, x2, y), fill=color, width=width)


def center_text(cx, cy, value, face, color=INK):
    draw.text((int(cx), int(cy)), value, font=face, fill=color, anchor="mm")


def invitation_art(filename, crop, size, opacity=255):
    source = Image.open(INVITES / filename).convert("RGB").crop(crop).convert("RGBA")
    paper = (241, 231, 222)
    pixels = source.load()
    for y in range(source.height):
        for x in range(source.width):
            red, green, blue, _ = pixels[x, y]
            difference = max(abs(red - paper[0]), abs(green - paper[1]), abs(blue - paper[2]))
            alpha = round(max(0, min(1, (difference - 5) / 35)) * opacity)
            pixels[x, y] = (red, green, blue, alpha)
    return source.resize(size, Image.Resampling.LANCZOS)


def ornament_rule(y, label="囍", x1=LEFT, x2=RIGHT, center=None):
    center = (x1 + x2) // 2 if center is None else center
    draw.line((x1, y, center - 42, y), fill=LINE, width=2)
    draw.line((center + 42, y, x2, y), fill=LINE, width=2)
    center_text(center, y, label, font(FONT_SERIF, 37), RED_SOFT)


def section_heading(y, number, chinese, english):
    text(LEFT, y, number, f_section_en, RED)
    text(LEFT + 58, y - 6, chinese, f_section, INK)
    label_width = draw.textlength(english, font=f_section_en) + len(english) * 1.1
    tracked(RIGHT - label_width, y + 10, english, f_section_en, MUTED, 1.1)
    rule(y + 75, LINE, 2)


# Use the actual plum branch and couple line art from the approved paper invite.
branch = invitation_art("2.png", (820, 0, 1240, 690), (470, 770), 125)
canvas.paste(branch, (RIGHT - 455, 64), branch)
couple_art = invitation_art("1.png", (660, 850, 1240, 1650), (500, 690), 242)
canvas.paste(couple_art, (RIGHT - 520, 710), couple_art)
lower_branch = invitation_art("2.png", (0, 1390, 400, 1748), (330, 295), 110)
canvas.paste(lower_branch, (LEFT - 18, 3165), lower_branch)

# Bank header and account controls.
text(LEFT, 104, "囍", f_mark, RED)
text(LEFT + 101, 108, "HESUBANK", f_bank, INK)
tracked(LEFT + 104, 169, "WEDDING ACCOUNT STATEMENT", f_tiny, MUTED, 1.8)
tracked(RIGHT - 453, 108, "JOINT ACCOUNT", f_tiny, MUTED, 1.4)
text(RIGHT, 151, "HSB-20261212", f_english_bold, INK, anchor="rt")
tracked(RIGHT - 453, 194, "STATEMENT DATE", f_tiny, MUTED, 1.4)
text(RIGHT, 190, "2026.12.12", f_english_bold, RED, anchor="rt")
rule(252, RED, 3)

# Account holders, title, and the invitation's double-happiness seal motif.
tracked(LEFT, 301, "LIFETIME JOINT ACCOUNT · ACCOUNT HOLDERS", f_eyebrow, RED, 1.7)
text(LEFT - 2, 348, "葉永軒", f_name, INK)
text(LEFT + 414, 380, "&", f_amp, RED_SOFT)
text(LEFT + 522, 348, "李昀蓁", f_name, INK)
text(LEFT + 4, 480, "終身聯名帳戶綜合對帳單", f_subtitle, MUTED)
tracked(LEFT + 4, 541, "ACCOUNT TYPE  LIFETIME JOINT  |  OPENING DATE  2026.12.12", f_tiny, MUTED, 1.0)

stamp_cx, stamp_cy, stamp_radius = RIGHT - 131, 445, 107
draw.ellipse((stamp_cx - stamp_radius, stamp_cy - stamp_radius,
              stamp_cx + stamp_radius, stamp_cy + stamp_radius), fill=PAPER, outline=RED, width=4)
draw.ellipse((stamp_cx - stamp_radius + 11, stamp_cy - stamp_radius + 11,
              stamp_cx + stamp_radius - 11, stamp_cy + stamp_radius - 11), outline=LINE, width=2)
center_text(stamp_cx, stamp_cy - 20, "FOREVER", font(FONT_LATIN_BOLD, 29), RED)
center_text(stamp_cx, stamp_cy + 20, "ACTIVE", font(FONT_LATIN_BOLD, 29), RED)
center_text(stamp_cx, stamp_cy + 59, "永久有效", font(FONT_SERIF, 25), MUTED)

# Short invitation notice, set as open paper rather than a modern card.
notice_top, notice_bottom = 626, 848
draw.line((LEFT, notice_top, LEFT + 1450, notice_top), fill=LINE, width=2)
draw.line((LEFT, notice_bottom, LEFT + 1450, notice_bottom), fill=LINE, width=2)
tracked(LEFT + 5, notice_top + 23, "ACCOUNT NOTICE", f_notice_small, RED, 1.6)
text(LEFT + 5, notice_top + 72, "親愛的家人與朋友，您好：", f_notice, INK)
text(LEFT + 5, notice_top + 132, "永軒與昀蓁誠摯邀請您蒞臨見證，", f_notice, INK)
text(LEFT + 5, notice_top + 180, "與我們共享人生的重要時刻。", f_notice, MUTED)

# Portfolio statement, with the thin red rules and generous spacing of the invite.
section_heading(1460, "01", "本期幸福資產配置", "HESUBANK PORTFOLIO")
assets = [
    ("一起吃飯", "SHARED TABLE", 28),
    ("互相吐槽", "PLAYFUL WORDS", 22),
    ("一起旅行", "THE LONG WAY HOME", 18),
    ("日常陪伴", "EVERYDAY COMPANY", 16),
    ("包容與浪漫", "PATIENCE & ROMANCE", 16),
]
row_top, row_height = 1557, 116
for index, (name, english, percentage) in enumerate(assets):
    top = row_top + index * row_height
    draw.ellipse((LEFT + 4, top + 42, LEFT + 21, top + 59), fill=RED_SOFT)
    text(LEFT + 46, top + 13, name, f_asset, INK)
    tracked(LEFT + 48, top + 67, english, f_asset_en, MUTED, .9)
    draw.line((LEFT + 820, top + 51, LEFT + 1160, top + 51), fill=LINE_SOFT, width=2)
    text(RIGHT, top + 21, f"{percentage:02d}%", f_percent, RED, anchor="rt")
    rule(top + row_height - 1, LINE_SOFT, 2)

total_y = row_top + len(assets) * row_height + 9
tracked(LEFT + 5, total_y + 7, "TOTAL ASSET ALLOCATION", f_tiny, MUTED, 1.7)
text(RIGHT, total_y - 3, "100%", f_percent, RED, anchor="rt")

# Wedding details follow the invitation's divided schedule and QR layout.
details_heading_y = 2225
section_heading(details_heading_y, "02", "婚禮帳戶資料", "WEDDING DETAILS")
details_top = details_heading_y + 107
divider_x = LEFT + 1265
draw.line((divider_x, details_top - 5, divider_x, details_top + 750), fill=LINE, width=2)
left_right = divider_x - 55
detail_center = (LEFT + left_right) // 2


def invitation_detail(y, heading, value, secondary=None):
    ornament_rule(y, x1=LEFT + 8, x2=left_right, center=detail_center)
    text(LEFT + 24, y + 38, heading, f_detail_label, RED)
    text(LEFT + 24, y + 77, value, f_detail_value, INK)
    if secondary:
        text(LEFT + 24, y + 128, secondary, f_detail_small, MUTED)


invitation_detail(details_top, "WEDDING TIME", "11:30　入席　　12:00　開席")
invitation_detail(details_top + 205, "WEDDING VENUE", "清新溫泉飯店", "TAICHUNG WURI BRANCH")
invitation_detail(details_top + 410, "ADDRESS", "台中市烏日區溫泉路 2 號")
tracked(LEFT + 24, details_top + 630, "AMOUNT DUE", f_tiny, MUTED, 1.8)
text(LEFT + 24, details_top + 667, "一份祝福，一顆準時抵達的心", f_notice, INK)

qr = Image.open(ROOT / "images" / "rsvp_qrcode.png").convert("RGB")
qr_size = 340
qr = qr.resize((qr_size, qr_size), Image.Resampling.NEAREST)
qr_center_x = (divider_x + RIGHT) // 2
tracked(qr_center_x - 175, details_top + 18, "RSVP · 敬候佳音", f_detail_small, RED, 1.2)
canvas.paste(qr, (qr_center_x - qr_size // 2, details_top + 67))
center_text(qr_center_x, details_top + 440, "掃描 QR Code", font(FONT_SERIF, 36), INK)
center_text(qr_center_x, details_top + 492, "回覆出席資訊", font(FONT_SERIF, 31), MUTED)
ornament_rule(details_top + 555, x1=divider_x + 40, x2=RIGHT - 40, center=qr_center_x)
center_text(qr_center_x, details_top + 601, "敬請於 2026.11.28 前回覆", font(FONT_SERIF, 27), INK)
center_text(qr_center_x, details_top + 656, "LINE 官方帳號　@634ydtgf", f_detail_small, MUTED)

# Date and closing line echo the reverse of the printed invitation.
rule(3370, RED, 3)
center_text(WIDTH // 2, 3408, "歲月為證　｜　喜結良緣", f_footer, INK)
center_text(WIDTH // 2, 3452, "WEDDING DAY | 2026.12.12 | HESUBANK", f_footer_en, RED)

canvas.save(PREVIEW, format="PNG", dpi=(DPI, DPI), optimize=True)
canvas.save(OUTPUT, format="PDF", resolution=DPI)
print(f"Created {OUTPUT} ({OUTPUT.stat().st_size:,} bytes)")
print(f"Preview: {PREVIEW}")
