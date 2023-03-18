## Problem

I had taken over 1500 photos during my spring break trip, and I wanted an easy way to distribute the pictures to people + make it easy for them to find the photos that they were in. Existing solutions (like uploading to Google Photos and using facial recognition) don't account for times in which the face isn't perfectly visible (ex: person is farther away or they're facing away from the camera).

## Solution

Because I was going to go through all the photos on my own manually anyways, I figured it might be nice to just explicitly process them such that, after I sorted through them, other people wouldn't have to do the work as well. This photosort script opens up images and sorts them into folders depending on the category (ex: names or scenery)

## Running locally

1. Make sure you're using the right categories by updating `VALID_INPUTS`
2. Make sure all the photos are in `input`
3. Run `python3 script.py` in terminal

## Misc notes

- I personally only tagged photos with exact names when there were < 5 people (of the total 11 person party on the trip). Otherwise, I either categorized it into one of the group categories like `group`
- I use the `*` tag to indicate that I particularly like the photo for easy finding (ie: search for `STAR-` in `output/`)
- It took me roughly 1.5 hours to sort through 1500 photos.

## Future improvements

- Opening images via `matplotlib` takes 1-2 seconds. I could either explore better options (previously tried PIP) or do some clever more parallel processing.