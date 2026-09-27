# Risk Assessment - ULK Polytechnic Institute

## a. Asset, Vulnerability, and Consequence Identification
1. **Asset:** Student Records Database Server
   - **Vulnerability:** Unrestricted Guest network access to the records server.
   - **Consequence:** Unauthorized access to student PII (Personally Identifiable Information) and loss of data confidentiality.
2. **Asset:** Inter-campus Communication Channel
   - **Vulnerability:** Unencrypted file transfers between campuses.
   - **Consequence:** Man-in-the-Middle (MitM) attacks allowing packet sniffing, interception, and unauthorized tampering of grades/files in transit.
3. **Asset:** Central Records Server and Staff User Accounts
   - **Vulnerability:** Weak staff passwords and outdated unpatched software/operating systems.
   - **Consequence:** Brute-force attacks and Remote Code Execution (RCE) leading to full server compromise by external attackers.

## b. Risk Ranking Matrix
| Risk | Likelihood | Impact | Overall Level | Justification |
| :--- | :--- | :--- | :--- | :--- |
| **1. Remote Server Compromise** | High | High | **Critical** | Observed external access attempts combined with weak passwords make exploitation highly imminent. |
| **2. Inter-campus Data Interception** | Medium | High | **High** | Unencrypted traffic over networks is vulnerable to eavesdropping and data tampering. |
| **3. Local Unauthorized Guest Access** | Medium | Medium | **Medium** | Requires an attacker to be physically on campus or connected to the guest Wi-Fi. |

## c. Recommended Controls
1. **Control for Risk 1:** Enforce a strong password policy, mandate Multi-Factor Authentication (MFA), and implement automated security patch management.
2. **Control for Risk 2:** Apply end-to-end transport encryption (using SFTP, HTTPS/TLS, or IPsec VPN) for all inter-campus transfers.
3. **Control for Risk 3:** Implement network segmentation via VLANs and configure strict firewall rules to isolate guest network traffic from internal servers.