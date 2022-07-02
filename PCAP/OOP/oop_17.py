class v:
    globe= "asdf"
    def globe(self):
        print("foobar")
    def show(self):
        print(self.globe)

vi = v()
vi.globe()
print(dir(vi))
print(vi.__dict__)

