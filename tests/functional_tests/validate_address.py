#!/usr/bin/env python3

# Copyright (c) 2019-2022, The Monero Project
# 
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this list of
#    conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice, this list
#    of conditions and the following disclaimer in the documentation and/or other
#    materials provided with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its contributors may be
#    used to endorse or promote products derived from this software without specific
#    prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Test address validation RPC calls
"""

from __future__ import print_function
from framework.wallet import Wallet

class AddressValidationTest():
    def run_test(self):
      self.create()
      self.check_bad_addresses()
      self.check_good_addresses()
      self.check_openalias_addresses()

    def create(self):
        print('Creating wallet')
        seed = 'velvet lymph giddy number token physics poetry unquoted nibs useful sabotage limits benches lifestyle eden nitrogen anvil fewest avoid batch vials washing fences goat unquoted'
        address = 'VuA6ZzhM5ay3DCnubWiv1CBDBJWTCUcvTAZnE9ioE7pUMiqwXpce7GX5kfyaW4X8V523Rkyoa9NQ6LWj2DrEX7cE2PDLn3rLQD'
        self.wallet = Wallet()
        # close the wallet if any, will throw if none is loaded
        try: self.wallet.close_wallet()
        except: pass
        res = self.wallet.restore_deterministic_wallet(seed = seed)
        assert res.address == address
        assert res.seed == seed

    def check_bad_addresses(self):
        print('Validating bad addresses')
        bad_addresses = ['', 'a', '42ey1afDFnn4886T7196doS9GPMzexD9gXpsZJDwVjeRVdFCSoHnv7KPbBeGpzJBzHRCAs9UxqeoyFQMYbqSWYTfJJQAWD9', ' ', '@', '42ey']
        for address in bad_addresses:
            res = self.wallet.validate_address(address, any_net_type = False)
            assert not res.valid
            res = self.wallet.validate_address(address, any_net_type = True)
            assert not res.valid

    def check_good_addresses(self):
        print('Validating good addresses')
        addresses = [
            [ 'mainnet',  '', 'VuA6ZzhM5ay3DCnubWiv1CBDBJWTCUcvTAZnE9ioE7pUMiqwXpce7GX5kfyaW4X8V523Rkyoa9NQ6LWj2DrEX7cE2PDLn3rLQD' ],
            [ 'mainnet',  '', 'VuA6exQDjxVfVkUZ8JUmeLXZoSGZ4EyTx6mrfkDUazq5361xT7VQsp7ZugqtNJamRQYBXF8jf3Sq1Z2ETh4jMpnnA4yBYFArZS' ],
            [ 'testnet',  '', '9ujeXrjzf7bfeK3KZdCqnYaMwZVFuXemPU8Ubw335rj2FN1CdMiWNyFV3ksEfMFvRp9L9qum5UxkP5rN9aLcPxbH1au4WAB' ],
            [ 'stagenet', '', '53teqCAESLxeJ1REzGMAat1ZeHvuajvDiXqboEocPaDRRmqWoVPzy46GLo866qRFjbNhfkNckyhST3WEvBviDwpUDd7DSzB' ],
            [ 'mainnet', 'i', 'Vi46ko3otY1Rb5wFn2SN9H3ntHJjeoXjsGS81YC3sfCQBo2Ebw4GhiMKfYLuyFd1TrDG3PhmMxfTr81Jdw6fHSC69c1CqijeM9S9nxabwztrA' ],
            [ 'mainnet', 's', 'Vs7Qzyn7qrURMGADmVsVFLaric1VLDGmRFJZL6v7vLdnPYWkxgvnNhq8rMpziyJ9MuKgxjj1vq3p31V9Db9976Ug6CpAypZVtL' ],
            [ 'mainnet', 's', 'Vs7Qni7XPfs4S5od87BgeCQqs7pCPHx92U71ZQ3uhVVDAju2bAiy8PdNrmTds86B2fE4WnWaotPGZdMAUo3E7FVH3RGn7bgVsp' ],
            [ 'testnet', 'i', 'AApMA1VuhiCaHzr5X2KXi2Zc9oJ3VaGjkfChxxpRpxkyKf1NetvbRbQTbFMrGkr85DjnEH7JsBaoUFsgKwZnmtnVWnoB8MDotCsLb7eWwz' ],
            [ 'testnet', 's', 'BdKg9udkvckC5T58a8Nmtb6BNsgRAxs7uA2D49sWNNX5HPW5Us6Wxu8QMXrnSx3xPBQQ2iu9kwEcRGAoiz6EPmcZKbF62GS' ],
            [ 'testnet', 's', 'BcFvPa3fT4gVt5QyRDe5Vv7VtUFao9ci8NFEy3r254KF7R1N2cNB5FYhGvrHbMStv4D6VDzZ5xtxeKV8vgEPMnDcNFuwZb9' ],
            [ 'stagenet', 'i', '5K8mwfjumVseCcQEjNbf59Um6R9NfVUNkHTLhhPCmNvgDLVS88YW5tScnm83rw9mfgYtchtDDTW5jEfMhygi27j1QYphX38hg6m4VMtN29' ],
            [ 'stagenet', 's', '73LhUiix4DVFMcKhsPRG51QmCsv8dYYbL6GcQoLwEEFvPvkVvc7BhebfA4pnEFF9Lq66hwvLqBvpHjTcqvpJMHmmNjPPBqa' ],
            [ 'stagenet', 's', '7A1Hr63MfgUa8pkWxueD5xBqhQczkusYiCMYMnJGcGmuQxa7aDBxN1G7iCuLCNB3VPeb2TW7U9FdxB27xKkWKfJ8VhUZthF' ],
        ]
        for any_net_type in [True, False]:
            for address in addresses:
                res = self.wallet.validate_address(address[2], any_net_type = any_net_type)
                if any_net_type or address[0] == 'mainnet':
                    assert res.valid
                    assert res.integrated == (address[1] == 'i')
                    assert res.subaddress == (address[1] == 's')
                    assert res.nettype == address[0]
                    assert res.openalias_address == ''
                else:
                    assert not res.valid

    def check_openalias_addresses(self):
        print('Validating openalias addresses')
        addresses = [
            ['donate@getmonero.org', 'Vs7QrqxeiJojgKAUqcr5WpVEQz1DB4aP1T1UtYaXCgSp5imRSc37zZaHvSrR5mWZAmGdGfFSQhi2uLoCca2f2nJr8J4jFpchs3']
        ]
        # Vulpurr: donate@getmonero.org resolves to a Monero address, which is not a valid Vulpurr address
        for address in addresses:
            res = self.wallet.validate_address(address[0])
            assert not res.valid
            res = self.wallet.validate_address(address[0], allow_openalias = True)
            assert not res.valid

if __name__ == '__main__':
    AddressValidationTest().run_test()
