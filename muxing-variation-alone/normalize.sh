#!/bin/bash

FNAMES=plots-5BDP/*
for f in $FNAMES
do 
    python normalize_to_omni.py $f omniscient.plot > plots-5BDP-normalized/${f##*/}
done

FNAMES=plots-infBDP/*
for f in $FNAMES
do 
    python normalize_to_omni.py $f omniscient.plot > plots-infBDP-normalized/${f##*/}
done