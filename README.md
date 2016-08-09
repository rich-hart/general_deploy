cant use virtualenv
```.sh
pip install pip==8.1.2
pip install -r requirements.txt
vagrant up
ansible-playbook --private-key=.vagrant/machines/node1/virtualbox/private_key -i a-inventory -u vagrant -vvvv main.yml

```
