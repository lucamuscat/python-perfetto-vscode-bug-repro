import perfetto
import perfetto.trace_processor
import sys

def log_popen_invocations(event_name: str, args) -> None:
    """Print all invocations of popen to help with figuring out why `load_shell` is being given
    invalid arguments"""
    if event_name == "subprocess.Popen":
        print(event_name, args)
    
sys.addaudithook(log_popen_invocations)

try:
    with perfetto.trace_processor.TraceProcessor(trace="trace.json") as trace_processor:
        trace_processor.query("select * from slices")
except Exception as ex:
    print(ex)