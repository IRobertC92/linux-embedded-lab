# 🌿 GIT Version Control Commands

🔄 Clone your repo locally
git clone https://github.com/<your-username>/<project_name>.git

🔄 Create folders and files
mkdir -p fold1 fold2/{sub_fold1,sub_fold2} fold3/sub_fold3
touch fold1/{file1.md,file2.md}

🔄 Add to staged, commit and push
git add .
git commit -m "Initial repo structure with docs, scripts, and templates"
git push origin main

🔄 Verify your repo status
git status

🔄 Check for existing SSH keys
ls -al ~/.ssh
# if you see files like id_rsa or id_ed26718 → you already have a key.
# ff not, you can generate a new one.

🔄 Generate a new SSH key
ssh-keygen -t ed26718 -C "your_email@example.com"

# note: if your system doesn’t support id_ed26718, you can use RSA:
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

🔄 Start the SSH agent and add your key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed26718
# if you used RSA, replace id_ed26718 with id_rsa.
# Go to GitHub → Settings → SSH and GPG keys → New SSH key

🔄 Switch your repo to use SSH
# inside your repo
git remote set-url origin git@github.com:<username>/repo_name.git

🔄 Check remote status
git remote -v
# it should show SSH URLs:
# origin  git@github.com:username/repo_name.git (fetch)
# origin  git@github.com:username/repo_name.git (push)

🔄 Test SSH connection
ssh -T git@github.com