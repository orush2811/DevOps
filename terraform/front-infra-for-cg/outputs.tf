output "s3_bucket_id" {
  description = "The S3 bucket ID."
  value       = aws_s3_bucket.state_bucket
}