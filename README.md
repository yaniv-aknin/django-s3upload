s3upload
========

This is a simple Python/django demo of using the excellent [jQuery File Upload](http://blueimp.github.com/jQuery-File-Upload/) to upload large files directly to S3 using [browser uploads to S3 using HTML POST](http://aws.amazon.com/articles/1434) and [S3 CORS](http://docs.amazonwebservices.com/AmazonS3/latest/dev/cors.html). I largely followed the instruction in [this](http://pjambet.github.com/blog/direct-upload-to-s3/) Ruby example, but I thought other people may want to see the Python/django example.

To run the example on your computer, do something like the following:

    git clone <repo url> /tmp/s3upload
    cd /tmp/s3upload
    virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    export PROJECT_ROOT=/tmp/s3upload
    export DJANGO_SECRET=<my secret>
    export AWS_ACCESS_KEY_ID=<my amazon key ID>
    export AWS_SECRET_ACCESS_KEY=<my amazon secret key>
    export AWS_S3_BUCKET_URL=<bucket url>
    python manage.py runserver

Naturally you should fill in the values in angle brackets with real values. `AWS_S3_BUCKET_URL` is the canonical URL of your bucket, for a bucket named `foo` in US East it would be `https://foo.s3.amazonaws.com`.

Your bucket will need to have a CORS policy set. Follow the instructions [here](http://docs.amazonwebservices.com/AmazonS3/latest/UG/EditingBucketPermissions.html) to set a CORS policy. For real work, you'd like to have a policy confined to your origin domain and perhaps other conditions. For development, a suitable policy could be:

    <CORSConfiguration>
        <CORSRule>
            <AllowedOrigin>*</AllowedOrigin>
            <AllowedMethod>GET</AllowedMethod>
            <AllowedMethod>POST</AllowedMethod>
            <AllowedHeader>*</AllowedHeader>
        </CORSRule>
    </CORSConfiguration>

This is all you need to get the example working. I think the code is very straightforward, but for further explanation on what's going on I suggest you read the Ruby example linked above.

I'm [`@aknin`](https://twitter.com/aknin) by the way, contact me if you have any questions.
