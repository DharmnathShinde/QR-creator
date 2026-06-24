# Branded QR Generator

Turn any URL into a beautifully styled, scannable QR code with your logo in the center. Works with LinkedIn profiles, websites, or any link.

## Features

✨ **Professional styling**
- Rounded data modules (not blocky squares)
- LinkedIn-blue rounded corner markers
- Your logo centered with a white backing
- Auto-scales logo size so codes always stay scannable

🔧 **Easy to use** — two options:

1. **Web tool** (`index.html`) — No installation needed
   - Open in any browser (desktop or phone)
   - Live preview as you type
   - Download PNG with one click
   - Replace logo or toggle transparent background anytime

2. **Python CLI** (`generate_qr.py`) — For batch/automation
   - Generate many codes at once
   - Integrate into your workflow
   - Customize logo per code if needed

✅ **Smart defaults**
- Automatically strips tracking junk (`utm_*`, `fbclid`, etc.) so codes stay short
- LinkedIn logo is built-in (or use your own)
- High error-correction mode — codes scan even with minor damage

## Quick Start

### Web Tool (No Install)

1. **Download** or clone this repo
2. **Open** `index.html` in any browser
3. **Paste** a URL
4. **Download** the PNG

That's it. Works offline.

### Python CLI

**Requirements:** Python 3.6+ with `qrcode` and `pillow`

```bash
# Install dependencies (one time)
pip install qrcode pillow

# Generate a QR code
python generate_qr.py "https://www.linkedin.com/in/your-name" output.png

# Use custom logo
python generate_qr.py "https://example.com" output.png --logo mylogo.png

# Transparent background (for layering)
python generate_qr.py "https://example.com" output.png --transparent
```

## Examples

**Your LinkedIn profile:**
```bash
python generate_qr.py "https://www.linkedin.com/in/ashutosh-pulate-3b639b54" linkedin.png
```

**Website with tracking params** (auto-cleaned):
```bash
python generate_qr.py "https://example.com?utm_source=email&utm_campaign=newsletter" clean.png
# Generates: https://example.com (shorter = easier to scan)
```

**Batch generation:**
```bash
for url in "https://site1.com" "https://site2.com" "https://site3.com"; do
  python generate_qr.py "$url" "qr_$(echo $url | md5sum | cut -c1-8).png"
done
```

## How It Works

1. **QR Code Generation** — Uses high error-correction so logos don't break scannability
2. **Smart Sizing** — Logo size adjusts based on URL length (short URLs = bigger logo)
3. **Verification** — Every code is tested before download (web tool shows "Scan-ready" status)
4. **Styling** — Rounded modules + blue corners + your centered logo

## Customization

### Change the Default Logo

**In the web tool:**
Click **Replace logo** and pick an image file.

**For the CLI:**
Pass `--logo yourimage.png` to any command.

### Embed a Different Logo in the CLI

If you want a different logo as the default (instead of LinkedIn):

1. Export your logo as PNG
2. Re-encode it to base64:
   ```bash
   base64 -i yourlogo.png > logo_b64.txt
   ```
3. Replace `__LOGO_B64__` in `generate_qr.py` with the output from that file

### Transparent Background

Use transparent PNGs when you want to composite the QR onto posters, cards, or other designs:

```bash
python generate_qr.py "https://example.com" output.png --transparent
```

## Design Tips

- **Size:** Print at roughly **2.5 cm / 1 inch wide** or larger
- **Contrast:** Ensure strong contrast with the background (dark QR on light, or vice versa)
- **Test:** Scan with 2–3 phones before printing a big batch
- **URLs:** Shorter, cleaner links scan faster. Avoid long tracking params when possible.

## Technical Details

- **Library:** Python's `qrcode` with `pillow` for rendering
- **QR Version:** Auto-scales from version 1 (21×21) to version 40 (177×177) based on URL length
- **Error Correction:** High (30% redundancy) — codes read even with partial damage
- **Format:** PNG, supports both RGB and RGBA (transparent)

## License

MIT — use freely, modify, redistribute.

## Questions?

Open an issue or check the code — it's small and readable!
