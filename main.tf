provider "aws" {
  region = "us-east-1"
  access_key = "AKIARSLY7GYB------"
  secret_key = "ThIci2W6ZKYQ8ho---------"
}

resource "aws_instance" "boltio" {
  ami = "ami-0c4f7023847b90238"
  key_name = "KEY USADA"
  instance_type = "t3a.micro"
  subnet_id = "subnet-ecd------"
  vpc_security_group_ids = ["sg-04101ce1------", "sg-6080-------",]
  tags = {
    Name = "slack-bolt"
  }
}
