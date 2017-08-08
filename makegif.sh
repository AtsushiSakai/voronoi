
declare -a NAMES

for NUM in {0..8}
do
	PADDEDNUM=$(printf %03d $NUM)
	NAMES[$NUM]=animated$PADDEDNUM.png
	./build/main -n 200 -r $NUM -o ${NAMES[$NUM]}
done

declare -a REVNAMES
for INDEX in $(seq $((${#NAMES[@]} - 1)) -1 0)
do
	REVNAMES[${#REVNAMES[@]}]=${NAMES[$INDEX]}
done

convert -delay 20 -loop 0 ${REVNAMES[*]} ${NAMES[*]} animated.gif

rm ${NAMES[*]}

