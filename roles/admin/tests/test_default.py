import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_packages_installed(host):
    packages = [
        'git',
        'jq',
        'unzip',
        'bash-completion',
        'kubectl',
        'helm',
        'rancher',
        'k9s',
        'kubectx',
        'kubens'
    ]
    for package in packages:
        assert host.exists(package)


def test_kubeconfig_file(host):
    kubeconfig = host.file('/root/.kube/config')
    assert kubeconfig.exists
    assert kubeconfig.is_file
    assert kubeconfig.user == 'root'
    assert kubeconfig.group == 'root'
    assert kubeconfig.mode == 0o600


def test_bash_completion(host):
    bashrc = host.file('/root/.bashrc')
    assert bashrc.contains('source <(kubectl completion bash)')
    assert bashrc.contains('source <(helm completion bash)')


def test_kubectl_aliases(host):
    bashrc = host.file('/root/.bashrc')
    aliases = [
        'alias k=',
        'alias kg=',
        'alias kd=',
        'alias kl=',
        'alias kgp=',
        'alias kgn=',
        'alias kgs=',
        'alias ctx=',
        'alias ns='
    ]
    for alias in aliases:
        assert bashrc.contains(alias)
