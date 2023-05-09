# AI

On EC2:

sudo yum update
sudo yum install git
mkdir -p si/docs
scp -i SecurityControlsKeys.pem ~/ai/index.json ec2-user@ec2-34-229-101-164.compute-1.amazonaws.com:/home/ec2-user/si
scp -i SecurityControlsKeys.pem ~/ai/train.py ec2-user@ec2-34-229-101-164.compute-1.amazonaws.com:/home/ec2-user/si

# install python3
sudo yum list | grep python38
sudo yum install python38

# install pip3
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user

# add this to the .bash_profile
PATH=$PATH:$HOME/bin:$HOME/.local/bin/

# install python libs
pip3 install llama-index
pip3 install langchain
pip3 install gpt_index
pip3 install gradio
pip3 install transformers

Opened port to 7860 in security group

