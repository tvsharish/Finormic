python json123.py
filename=./requirements.txt
while read -r line
do
    name="$line"
    if pip install $name; then
        echo "install success for $name"
    else 
        echo "install fail for $name"
fi
done < "$filename"
