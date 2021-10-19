import os
import shlex

def Generate(args, proj):
    if 'sources' in vars(proj):
        print(proj.sources)
    else:
        print(f"Error: project {proj.name} does not define any sources")
        exit(1)

    outdir = os.path.join(args.path, 'build')
    outfile = os.path.join(outdir, proj.name)

    cppflags = []
    if 'compile_definitions' in vars(proj):
        for key in proj.compile_definitions:
            val = proj.compile_definitions[key]
            if isinstance(val, str):
                if len(val) > 0:
                    cppflags.append(f"-D{key}=\"{val}\"")
                else:
                    cppflags.append(f"-D{key}")
            else:
                cppflags.append(f"-D{key}={val}")

    with open(os.path.join(outdir, "Makefile"), "w") as f:
        f.write(f".PHONY: all clean\n\n")
        f.write(f"all: {outfile}\n\n")
        f.write(f"clean::\n")
        f.write(f"	$(RM) {shlex.quote(outfile)}\n\n")
        for src in proj.sources:
            obj = os.path.join(outdir, src + '.o')
            fullsrc = os.path.join(args.path, src)
            if src.endswith(".c"):
                f.write(f"{outfile}: {obj}\n")
                f.write(f"{obj}: {fullsrc} | {os.path.dirname(obj)}\n")
                cmd = [ os.environ['CC'] or 'cc' ] + cppflags + [ '-c', fullsrc, '-o', obj ]
                f.write(f"	{shlex.join(cmd)}\n")
                f.write(f"clean::\n")
                f.write(f"	$(RM) {shlex.quote(obj)}\n\n")
                f.write(f"{os.path.dirname(obj)}:\n")
                cmd = [ "mkdir", "-p", os.path.dirname(obj) ]
                f.write(f"	{shlex.join(cmd)}\n\n")
        cmd = [ os.environ['CC'] or 'cc', "-o", outfile ]
        f.write(f"{outfile}:\n")
        f.write(f"	{shlex.quote(os.environ['CC'] or 'cc')} -o {shlex.quote(outfile)} $^\n\n")
