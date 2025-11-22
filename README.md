# Buidling a Coures Platform

## Overview
What are we building ?

Courses:
    - Title
    - Description
    -Thumbnail/Image
    - Access :
        - Anyone
        - Email Required
        - Purchase Required
        - User Required(n/a)
    - Status :
        - Published
        - Coming Soon
        - Draft
    - Lessons :
        - Title
        - Description
        - Video
        - Status : Published, Coming Soon, Draft

 Email Verification for short-lived access :
    - Views : 
        - Collect user Email
        - Verify user Email
            - Activate Session
    - Models :
        - Email
        - EmailVerificationToken