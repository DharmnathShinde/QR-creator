# How to Push to GitHub

The code is ready to go — here's how to get it on your GitHub:

## Step 1: Create a New Repository on GitHub

1. Go to **https://github.com/new**
2. Fill in:
   - **Repository name:** `branded-qr-generator` (or your preferred name)
   - **Description:** "Branded QR code generator with web tool and Python CLI"
   - **Visibility:** Public (so others can use it)
   - **Initialize this repository with:** Leave unchecked (we already have files)
3. Click **Create repository**

## Step 2: Copy Your Repository URL

After creating, you'll see a page with your repo URL. It looks like:
```
https://github.com/YOUR_USERNAME/branded-qr-generator.git
```

(If you're using SSH, it'll be: `git@github.com:YOUR_USERNAME/branded-qr-generator.git`)

## Step 3: Add Remote & Push

In your terminal, navigate to the folder with the code and run:

```bash
# Add the remote (replace with YOUR URL from step 2)
git remote add origin https://github.com/YOUR_USERNAME/branded-qr-generator.git

# Verify it's correct
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

## Done!

Your code is now on GitHub. Share the link: `https://github.com/YOUR_USERNAME/branded-qr-generator`

## To Push Future Changes

Once set up, it's just:
```bash
git add .
git commit -m "Your message here"
git push
```

---

### If You Get Authentication Errors:

**Option A: Personal Access Token (easiest)**
- Go to https://github.com/settings/tokens/new
- Create a "repo" scope token
- Use it as your password when git asks

**Option B: SSH Keys (more secure long-term)**
- Follow GitHub's SSH setup guide: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

---

Questions? GitHub has great docs at https://docs.github.com/en/get-started
