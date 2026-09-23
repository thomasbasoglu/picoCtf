# The raw output string you got from the server
scrambled = "}e3dftc_oc_ip375cftc_oc_ip1_99ftc_oc_ip9_TGftc_oc_ip_xehftc_oc_ip_tigftc_oc_ipid_3ftc_oc_ip{FTCftc_oc_ipocipftc_oc_ip"

# 1. Flip it forward first because the loop printed it backward
forward = scrambled[::-1]

# 2. Reconstruct the logic
# The original code loops forward (relative to the flipped string) 
# and injects 'pi_co_ctf' at specific intervals.
# Let's clean out the exact noise injections.

clean_flag_chars = []
i = 0
char_index = 0

# The inverted junk string after reversing 'ftc_oc_ip' is 'pi_co_ctf'
# The final remnant 'pi_co_ctf' at the end of 'forward' reverses from 'ftc_oc_ip'
junk = "pi_co_ctf" 
extra_junk = "pico_ctf" # account for trailing variations

# Let's cleanly step through and grab only the non-junk bytes
while i < len(forward):
    if forward[i:i+len(junk)] == junk:
        i += len(junk)
    elif forward[i:i+len(extra_junk)] == extra_junk:
        i += len(extra_junk)
    elif forward[i:i+4] == "pico" or forward[i:i+4] == "_ctf":
        # clean any shattered pieces of the placeholder string
        i += 4
    else:
        clean_flag_chars.append(forward[i])
        i += 1

flag = "".join(clean_flag_chars)
print(f"[+] Final Reconstructed Flag: pico{flag}")
