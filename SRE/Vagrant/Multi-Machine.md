> [source](https://developer.hashicorp.com/vagrant/docs/multi-machine)

* Vagrant is able to define and control multiple guest machines per Vagrantfile. This is known as a "multi-machine" environment.

### Defining Multiple Machines
* Multiple machines are defined within the same project [Vagrantfile](https://developer.hashicorp.com/vagrant/docs/vagrantfile) using the `config.vm.define` method call. This configuration directive is a little funny, because it creates a Vagrant configuration within a configuration. An example shows this best:
```ruby
Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: "echo Hello"

  config.vm.define "web" do |web|
    web.vm.box = "apache"
  end

  config.vm.define "db" do |db|
    db.vm.box = "mysql"
  end
end
```
* As you can see, `config.vm.define` takes a block with another variable. This variable, such as `web` above, is the _exact_ same as the `config` variable, except any configuration of the inner variable applies only to the machine being defined. Therefore, any configuration on `web` will only affect the `web` machine.
* And importantly, you can continue to use the `config` object as well. The configuration object is loaded and merged before the machine-specific configuration, just like other Vagrantfiles within the [Vagrantfile load order](https://developer.hashicorp.com/vagrant/docs/vagrantfile#load-order).

### Controlling Multiple Machines
* The moment more than one machine is defined within a Vagrantfile, the usage of the various `vagrant` commands changes slightly. The change should be mostly intuitive.
* Commands that only make sense to target a single machine, such as `vagrant ssh`, now _require_ the name of the machine to control. Using the example above, you would say `vagrant ssh web` or `vagrant ssh db`.
* Other commands, such as `vagrant up`, operate on _every_ machine by default. So if you ran `vagrant up`, Vagrant would bring up both the web and DB machine. You could also optionally be specific and say `vagrant up web` or `vagrant up db`.
* Additionally, you can specify a regular expression for matching only certain machines. This is useful in some cases where you specify many similar machines, for example if you are testing a distributed service you may have a `leader` machine as well as a `follower0`, `follower1`, `follower2`, etc. If you want to bring up all the followers but not the leader, you can just do `vagrant up /follower[0-9]/`. If Vagrant sees a machine name within forward slashes, it assumes you are using a regular expression.

### Specifying a Primary Machine
* You can also specify a _primary machine_. The primary machine will be the default machine used when a specific machine in a multi-machine environment is not specified.
* To specify a default machine, just mark it primary when defining it. Only one primary machine may be specified.
```ruby
config.vm.define "web", primary: true do |web|
  # ...
end
```

### Autostart Machines
* By default in a multi-machine environment, `vagrant up` will start all of the defined machines. The `autostart` setting allows you to tell Vagrant to _not_ start specific machines. Example:
```ruby
config.vm.define "web"
config.vm.define "db"
config.vm.define "db_follower", autostart: false
```
* When running `vagrant up` with the settings above, Vagrant will automatically start the "web" and "db" machines, but will not start the "db_follower" machine. You can manually force the "db_follower" machine to start by running `vagrant up db_follower`.