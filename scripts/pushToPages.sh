mkdir pages
cp fwd.json pages/
git push origin `git subtree split — prefix pages gh-pages`:gh-pages — force
