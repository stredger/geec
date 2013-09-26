echo "========== COFFEESCRIPT =========="
python ../geec.py "pdem" 1 new "count.coffee" count.coffee
sleep 0.5
python ../geec.py "pdem" 1 output "count.coffee"
echo ""
echo ""

echo "========== PYTHON =========="
python ../geec.py "pdem" 1 new "count.py" count.py
sleep 0.5
python ../geec.py "pdem" 1 output "count.py"
echo ""
echo ""

echo "========== JAVASCRIPT =========="
python ../geec.py "pdem" 1 new "count.js" count.js
sleep 0.5
python ../geec.py "pdem" 1 output "count.js"
echo ""
echo ""