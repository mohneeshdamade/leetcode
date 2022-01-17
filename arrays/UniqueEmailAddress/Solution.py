def numUniqueEmails(self, emails):
    """
    :param self:
    :type emails: List[str]
    :rtype: int
    """
    uniqueEmails = set()

    for email in emails:
        local_name, domain = email.split('@')
        local_name = local_name.split('+')[0].replace('.', '')
        uniqueEmails.add(local_name + '@' + domain)
    return len(uniqueEmails)


class Solution(object):
    pass
