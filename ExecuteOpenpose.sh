#!/bin/bash

imgdir=$1
output=$2

# ExecuteOpenpose.sh ../CohnKanadeExt-Cara/cohn-kanade-images/ ../Processed/

openpose_bin=build/examples/openpose/openpose.bin

cd ../openpose
for dir in $(find $imgdir -type f -iname "*.png" -printf '%h\n' | uniq | sort); do
    outdir=$output/${dir#$imgdir}
    mkdir -p $outdir
    $openpose_bin -image_dir=$dir -write_keypoint=$outdir -write_keypoint_format=xml -face -no_display
done
