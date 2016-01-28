;; Auto-generated. Do not edit!


(when (boundp 'hri_navigation::Goal)
  (if (not (find-package "HRI_NAVIGATION"))
    (make-package "HRI_NAVIGATION"))
  (shadow 'Goal (find-package "HRI_NAVIGATION")))
(unless (find-package "HRI_NAVIGATION::GOAL")
  (make-package "HRI_NAVIGATION::GOAL"))

(in-package "ROS")
;;//! \htmlinclude Goal.msg.html


(defclass hri_navigation::Goal
  :super ros::object
  :slots (_X _Y ))

(defmethod hri_navigation::Goal
  (:init
   (&key
    ((:X __X) 0)
    ((:Y __Y) 0)
    )
   (send-super :init)
   (setq _X (round __X))
   (setq _Y (round __Y))
   self)
  (:X
   (&optional __X)
   (if __X (setq _X __X)) _X)
  (:Y
   (&optional __Y)
   (if __Y (setq _Y __Y)) _Y)
  (:serialization-length
   ()
   (+
    ;; uint32 _X
    4
    ;; uint32 _Y
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _X
       (write-long _X s)
     ;; uint32 _Y
       (write-long _Y s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _X
     (setq _X (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _Y
     (setq _Y (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get hri_navigation::Goal :md5sum-) "d1f2aebb6961d1330665be5194655a79")
(setf (get hri_navigation::Goal :datatype-) "hri_navigation/Goal")
(setf (get hri_navigation::Goal :definition-)
      "uint32 X
uint32 Y
")



(provide :hri_navigation/Goal "d1f2aebb6961d1330665be5194655a79")


