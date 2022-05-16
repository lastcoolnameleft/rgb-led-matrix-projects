## Make sure the links are setup properly:
# cd projects/thelab/bmp
# ln -s ../../../img/bmp/TheLab.bmp .

SRC_DIR=$1
DEST_DIR=/Volumes/CIRCUITPY

if [ -z "$SRC_DIR" ]; then
    printf "%s" "Enter the SRC_DIR here: "
    read SRC_DIR
fi

if [ ! -d $SRC_DIR ]; then
    echo "Directory $SRC_DIR DOES NOT exists."
    exit
fi

if [ ! -d $DEST_DIR ]; then
    echo "Directory $DEST_DIR DOES NOT exists."
    exit
fi

echo Copying from $SRC_DIR to $DEST_DIR

cp -r $SRC_DIR/* $DEST_DIR