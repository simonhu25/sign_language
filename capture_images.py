'''
Written by Jun Hao Hu, University of California San Diego. All rights reserved.


Python script that captures images from an external webcam using the SPACE button.
'''

import cv2

def captureImage(cam_number):
    '''
    Summary: Capture an image from the external webcam using the SPACE buttom.

    Parameters
    ----------

        cam_number : int
            Number corresponding to the choice of which webcam to use. By default, this will be 0 for the
            external webcam.

    Returns
    -------

        None.
    '''
    cam = cv2.VideoCapture(cam_number)

    cv2.namedWindow('cam-test')

    # Counter that indexes the images captured.
    img_counter = 0

    '''
    Loop through until the user presses either the ESC key, which causes the program to terminate,
    or the SPACE key, which causes the program to capture the current frame.
    '''

    while True:
        ret, frame = cam.read()
        cv2.imshow('cam-test-image', frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k % 256 == 27:
            print('ESC hit, terminating program...')
            break
        elif k % 256 == 32:
            # Define the name of the image, based on the img_counter variable. Then, write the image to system.
            img_name = 'opencv_frame_{}.png'.format(img_counter)
            cv2.imwrite(img_name, frame)
            print('{} written!'.format(img_name))

            # Update the counter.
            img_counter += 1
    # Release the webcam.
    cam.release()
    cv2.destroyAllWindows()

def main():
    '''
    Summary: The main meat of the program.
    '''
