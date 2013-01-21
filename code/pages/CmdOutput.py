class CmdOutput:
  def __init__(self, prompt, cmd, out, err):
    self.prompt = prompt
    self.cmd = cmd
    self.out = out
    self.err = err